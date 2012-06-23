from cnab240.registro import Registro

class Lote(object):
    HEADER_LOTE = None
    TRAILER_LOTE = None
    EVENTOS_VALIDOS = None
     
    def __init__(self, **kwargs):
        required_constants = (self.HEADER_LOTE, 
                              self.TRAILER_LOTE,
                              self.EVENTOS_VALIDOS)
        if not all(required_constants):
            raise NotImplementedError

        self.header = Registro(self.HEADER_LOTE, versao)
        self.trailer = Registro(self.TRAILER_LOTE, versao)

        self._eventos = []

    def __unicode__(self):
        pass
    
    def adicionar_evento(self, evento):
        if any(isintance(evento, cls) for cls in EVENTOS_VALIDOS):
            self._evento.append(evento)
 

class Evento(object):
    SEGMENTOS_VALIDOS = None
    
    def __init__(self, **kwargs):
        # TODO: validar SEGMENTOS_VALIDOS
        self.versao_layout = kwargs.get('versao')
        self._segmentos = []
       
    def adicionar_segmento(self, segmento):
        # TODO: validar segmento usando SEGMENTOS_VALIDOS
        pass
 
    def __unicode__(self):
        pass # TODO:

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
