
import os
import json

from glob import iglob
from decimal import Decimal, InvalidOperation
from collections import OrderedDict
from cnab240 import errors


class Campo(object):
    def __init__(self, spec):
        self.nome = spec.get('nome')
        self.inicio = spec.get('posicao_inicio') - 1
        self.fim = spec.get('posicao_fim') 
        self.digitos = self.fim - self.inicio
        self.formato = spec.get('formato', 'alfa')
        self.decimais = spec.get('decimais', 0)
        self.default = spec.get('default')
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


class RegistroBase(object):

    def fromdict(self, dict_):
        pass

    def carregar(self, registro_str):

        for campo in self._campos.values():

            valor = registro_str[campo.inicio:campo.fim].strip()
            if campo.formato == 'num' and campo.decimais:
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
        attrs = {'_campos': campos}
        cls_name = spec.get('nome').encode('utf8')

        campo_specs = spec.get('campos', {})
        for key in sorted(campo_specs.iterkeys()):
            campo = Campo(campo_specs[key])
            entrada = {campo.nome: campo}

            campos.update(entrada)
            attrs.update(entrada)
        
        return type(cls_name, (RegistroBase, ), attrs)
