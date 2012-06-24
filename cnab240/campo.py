
import errors

from decimal import Decimal


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
                self.default = Decimal('0') 
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
