
import os
import json

from glob import iglob
from decimal import Decimal, InvalidOperation
from collections import OrderedDict
from cnab240 import errors


class CampoBase(object):
    def __init__(self):
        self._valor = None

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        if self.formato == 'alfa':
            if not isinstance(valor, unicode):
                raise errors.TipoError(self, valor)
            if len(valor) > self.digitos:
                raise errors.NumDigitosExcedidoError(self, valor)

        elif self.decimais:
            if not isinstance(valor, Decimal):
                raise errors.TipoError(self, valor)
            
            num_decimais = valor.as_tuple().exponent * -1
            if num_decimais != self.decimais:
                raise errors.NumDecimaisError(self, valor)
            
            if len(str(valor).replace('.', '')) > self.digitos:
                raise errors.NumDigitosExcedidoError(self, valor)

        else:
            if not isinstance(valor, (int, long)):
                raise errors.TipoError(self, valor)
            if len(str(valor)) > self.digitos:
                raise errors.NumDigitosExcedidoError(self, valor)
        
        self._valor = valor
    

    def __unicode__(self):
        if not self._valor:
            raise errors.CampoObrigatorioError(self.nome)
        
        valor = self._valor
        if self.formato == 'alfa' or self.decimais:
            if self.decimais:
                valor = unicode(valor).replace('.', '')
            chars_faltantes = self.digitos - len(valor)
            return valor + (u' ' * chars_faltantes)

        return u'{0:0{1}d}'.format(valor, self.digitos)

    def __repr__(self):
        return unicode(self)

    def __set__(self, instance, value):
        self.valor = value

    def __get__(self, instance, owner):
        return self.valor


def criar_classe_campo(spec):

    nome = spec.get('nome')
    inicio =  spec.get('posicao_inicio') - 1
    fim = spec.get('posicao_fim') 

    attrs = {
        'nome': nome, 
        'inicio': inicio, 
        'fim': fim, 
        'digitos': fim - inicio,
        'formato': spec.get('formato', 'alfa'),
        'decimais': spec.get('decimais', 0),
        'default': spec.get('default'),
    }
    
    return type(nome.encode('utf8'), (CampoBase,), attrs)


class RegistroBase(object):
        
    def __new__(cls, **kwargs):
        campos = OrderedDict()
        attrs = {'_campos': campos}

        for Campo in cls._campos_cls.values():
            campo = Campo()
            campos.update({campo.nome: campo}) 
            attrs.update({campo.nome: campo})

        new_cls = type(cls.__name__, (cls, ), attrs)
        return super(RegistroBase, cls).__new__(new_cls, **kwargs)
    
    def __init__(self, **kwargs):
        self.fromdict(kwargs)

    def necessario(self):
        for campo in self._campos.values():
            eh_controle = campo.nome.startswith('controle_') or \
                                            campo.nome.startswith('servico_')
            if not eh_controle and campo.valor:
                return True

        return False

    def todict(self):
        data_dict = dict()
        for campo in self._campos.values():
            if campo.valor:
                data_dict[campo.nome] = campo.valor  
        return data_dict
    
    def fromdict(self, data_dict):
        for key, value in data_dict.items():
            if hasattr(self, key):
                setattr(self, key, value) 

    def carregar(self, registro_str):
        for campo in self._campos.values():
            valor = registro_str[campo.inicio:campo.fim].strip()
            if campo.decimais:
                exponente = campo.decimais * -1
                dec = valor[:exponente] + '.' + valor[exponente:]
                try:
                    campo.valor = Decimal(dec)
                except InvalidOperation:
                    raise # raise custom?

            elif campo.formato == 'num':
                try:
                    campo.valor = int(valor)
                except ValueError:
                    raise errors.TipoError(campo, valor)
            else:
                campo.valor = valor

    def __unicode__(self):
        return ''.join([unicode(campo) for campo in self._campos.values()])


class Registros(object):
    def __init__(self, specs_dirpath):
        # TODO: Validar spec: nome (deve ser unico para cada registro),
        #   posicao_inicio, posicao_fim, formato (alpha), decimais (0),
        #   default (zeros se numerico ou brancos se alfa)
        registro_filepath_list = iglob(os.path.join(specs_dirpath, '*.json'))

        for registro_filepath in registro_filepath_list:
            registro_file = open(registro_filepath)
            spec = json.load(registro_file)
            registro_file.close()

            setattr(self, spec.get('nome'), self.criar_classe_registro(spec))


    def criar_classe_registro(self, spec):
        campos = OrderedDict()
        attrs = {'_campos_cls': campos}
        cls_name = spec.get('nome').encode('utf8')

        campo_specs = spec.get('campos', {})
        for key in sorted(campo_specs.iterkeys()):
            Campo = criar_classe_campo(campo_specs[key])
            entrada = {Campo.nome: Campo}

            campos.update(entrada)
        
        return type(cls_name, (RegistroBase, ), attrs)

