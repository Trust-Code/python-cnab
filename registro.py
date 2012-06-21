
import os                                                                        
import json                                                                      
import errors
                                                                                 
from decimal import Decimal, InvalidOperation
from collections import OrderedDict

REGISTRO_SPECS = {}


class Campo(object):
    def __init__(self, spec):
        self.nome = spec.get('nome')
        self.inicio = spec.get('posicao_inicio') - 1
        self.fim = spec.get('posicao_fim') 
        self.digitos = self.fim - self.inicio
        self.formato = spec.get('formato', 'alfa')
        self.decimais = spec.get('decimais', 0)
        self.default = spec.get('default', None)
        
        if not self.default:
            if self.formato == 'alfa':
                self.default = u' ' * self.digitos
            elif self.decimais:
                self.default = Decimal('0' * self.digitos) 
            else:
                self.default = 0 

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
        if self._valor:
            valor = self._valor
        else:
            valor = self.default

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


class Registro(object):

    def __new__(cls, nome):
        
        spec = REGISTRO_SPECS.get(nome, {})
        campos = OrderedDict()
        attrs = {'_campos': campos}

        campo_specs = spec.get('campos', {})
        for key in sorted(campo_specs.iterkeys()):
            campo = Campo(campo_specs[key])
            campos.update({campo.nome: campo})
            attrs.update({campo.nome: campo})

        new_cls = type('Registro', (RegistroBase, ), attrs)
        return new_cls() 


class RegistroBase(object):

    def carregar(self, registro_str):
 
        for campo in self._campos.values():
            
            valor = registro_str[campo.inicio:campo.fim].strip()
            if campo.formato == 'num' and campo.decimais:
                dec = valor[:campo.decimais] + '.' + valor[campo.decimais:]
                try:
                    campo.valor = Decimal(dec)
                except InvalidOperation:
                    raise # raise custom? 

            elif campo.formato == 'num':
                try:
                    campo.valor = int(valor)
                except ValueError:
                    raise # raise custom? 
            else:
                campo.valor = valor

    def escreve(self):
        return ''.join([unicode(campo) for campo in self._campos.values()])  


cwd_path = os.path.abspath(os.path.dirname(__file__))                            
registros_dirpath = os.path.join(cwd_path, 'registros')                          
for registro_path in os.listdir(registros_dirpath):                              
    registro_file = open(os.path.join(registros_dirpath, registro_path))         
    # TODO: Validar spec: nome (deve ser unico para cada registro), 
    #   posicao_inicio, posicao_fim, formato (alpha), decimais (0), 
    #   default (zeros se numerico ou brancos se alfa)                           
    spec = json.load(registro_file)                                              
    REGISTRO_SPECS.update({os.path.splitext(registro_path)[0]: spec})            
    registro_file.close()      

