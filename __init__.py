from cnab240.registro import Registro

class Cnab240(object):

    def __init__(self, **kwargs):
        versao_layout = kwargs.get('versao')
        if not versao_layout:
            raise Exception

        self.header = Registro('header_arquivo', self.versao_layout)
        self.trailer = Registro('trailer_arquivo', self.versao_layout)

        self.lotes = []


    def __unicode__(self):
        if self.lotes.count() == 0:
            raise Exception
        count_lotes = self.lotes.count()
        count_registros = 0
        for lote in lotes:
            for evento in lote.eventos:
                registros += evento.segmentos.count()

        self.trailer.totais_quantidade_lotes = count_lotes
        self.trailer.totais_quantidade_registros = count_registros
        unicode(self.header):
        unicode(lote) for lote in lotes
        unicode(self.trailer)

    def adicionar_lote(self, lote):
        if not isinstance(lote, 'Lote'):
            raise Exception
        self.lotes.append(lote)


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

        self.eventos = []

    def __unicode__(self):
        if self.eventos.count() == 0:
            raise Exception
        unicode(self.header)
        unicode(evento) for evento in self.eventos
        unicode(self.trailer)
    
    def adicionar_evento(self, evento):
        if any(isintance(evento, cls) for cls in EVENTOS_VALIDOS):
            self.eventos.append(evento)


class Evento(object):
    SEGMENTOS_UTILIZADOS = None
    
    def __init__(self, **kwargs):
        # TODO: validar SEGMENTOS_VALIDOS
        self.versao_layout = kwargs.get('versao')
        self.segmentos = []
       
    def adicionar_segmento(self, segmento):
        # TODO: validar segmento usando SEGMENTOS_VALIDOS
        pass
 
    def __unicode__(self):
        pass # TODO: