
import cnab240

from decimal import Decimal
from collections import OrderedDict

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
            if self.formato == 'num':
                if self.decimais:
                    self.default = Decimal('0' * self.digitos) 
                else:
                    self.default = 0 
            else:
                self.default = u' ' * self.digitos

        self._valor = None
    
    @property    
    def valor(self):
        return self._valor 

    @valor.setter
    def valor(self, valor):
        if self.formato == 'num':
            if self.decimais:
                if isinstance(valor, Decimal):
                    if valor.as_tuple().exponent == self.digitos * -1:
                        self._valor = valor
                    else:
                        raise Exception # TODO
                else:
                    raise Exception # TODO 
            else:
                if isinstance(valor, int):
                    self._valor = valor
                else:
                    raise Exception #TODO
        else:
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


class ErrorAoLerCampo(Exception):
    #def __unicode__(self):
    #    TODO 
    pass


class Registro(object):

    def __new__(cls, nome):
        
        spec = cnab240.registro_specs.get(nome)
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

    def carrega(self, registro_str):
        """
        Exemplo de registro_str: 
00100000         212345678901234abcdefghijklmnopqrst028916000000014262X7TRACY TECNOLOGIA LTDA ME      BANCO DO BRASIL                         02012071322000012345608512345                                                                     
"""       
 
        for campo in self._campos.values():
            
            valor = registro_str[campo.inicio:campo.fim].strip()
            if campo.formato == 'num' and campo.decimais:
                try:
                    dec = valor[:campo.decimais] + '.' + valor[campo.decimais:]
                    campo.valor = Decimal(dec)
                except InvalidOperation:
                    raise ErrorAoLerCampo('Convertendo para decimal', 
                                          valor, campo_spec)

            elif campo.formato == 'num':
                try:
                    campo.valor = int(valor)
                except ValueError:
                    raise ErrorAoLerCampo('Convertendo para inteiro',
                                          valor, campo_spec)

    def escreve(self):
        return ''.join([unicode(campo) for campo in self._campos.values()])  

