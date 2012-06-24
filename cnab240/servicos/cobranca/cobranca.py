from cnab240.registro import Registro
from cnab240 import Evento

 
# XXX: Necessario?
class Cobranca(Evento):
    def __init__(self, **kwargs):
        super(Cobranca, self).__init__(**kwargs)
        

class CobrancaRemessa(Cobranca):
    SEGMENTOS_VALIDOS = ('P', 'Q', 'R', 'Y')

    def __init__(self, **kwargs):
        super(CobrancaRemessa, self).__init__(**kwargs)
        self.banco = kwargs.get('banco')
        if not self.banco:
            raise Exception
        
        self.conta = kwargs.get('conta')
        if not self.conta:
            raise Exception


class EntradaTitulo(CobrancaRemessa):
    SEGMENTOS_VALIDOS = CobrancaRemessa.SEGMENTOS_VALIDOS + ('S',)

    def __init__(self, **kwargs):
        super(EntradaTitulo, self).__init__(**kwargs)
        

EntradaTitulo({'banco': '001', 'conta': 123123, 's': 'lala'})
Instrucao({'banco': '001', 'conta': 1213213})
