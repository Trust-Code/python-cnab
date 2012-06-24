from cnab240.registro import Registro
from cnab240.evento import Evento

 
class CobrancaRemessa(Evento):
    SEGMENTOS_VALIDOS = ('P', 'Q', 'R', 'Y')

    def __init__(self, **kwargs):
        super(CobrancaRemessa, self).__init__(**kwargs)
        self.banco = kwargs.get('banco')
        self.versao = kwargs.get('versao')
        
        if not kwargs.has_key('versao'):
            raise TypeError('kwarg "versao" eh obrigatorio')

        if not self.banco:
            raise Exception
        
        self.conta = kwargs.get('conta')
        if not self.conta:
            raise Exception


class EntradaTitulo(CobrancaRemessa):
    SEGMENTOS_VALIDOS = CobrancaRemessa.SEGMENTOS_VALIDOS + ('S',)

    def __init__(self, **kwargs):
        super(EntradaTitulo, self).__init__(**kwargs)
        

