
class Cnab240Error(Exception):
    """Excessao base para o CNAB 240"""


class AtribuicaoCampoError(Cnab240Error): 
    """Tentativa de atribuicao de valor indevido ao campo""" 

    def __init__(self, campo, valor):
        self.campo = campo
        self.valor = valor
        super(AtribuicaoCampoError, self).__init__(self)
        
    def __unicode__(self):                
        return u'campo:{0} formato:{1} decimais:{2} digitos:{3} - valor:{4}'.\
            format( 
                self.campo.nome,    
                self.campo.formato, 
                self.campo.decimais,
                self.campo.digitos, 
                repr(self.valor),
            )


class NumDigitosExcedidoError(AtribuicaoCampoError):                             
    """Tentativa de atribuicao de valor mais longo que o campo suportaia"""      
                                                                                 

class TipoError(AtribuicaoCampoError):                                           
    """Tentativa de atribuicao de tipo nao suportado pelo campo"""


class NumDecimaisError(AtribuicaoCampoError):
    """Numero de casasa decimais em desacordo com especificacao"""


