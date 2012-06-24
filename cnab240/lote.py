
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
            raise Exception # TODO: raise exception
    
        result = [] 
        result.append(unicode(self.header))
        result.extend(unicode(evento) for evento in self.eventos)
        result.append(unicode(self.trailer))
        return '\n'.join(result)
    
    def adicionar_evento(self, evento):
        if any(isintance(evento, cls) for cls in EVENTOS_VALIDOS):
            self.eventos.append(evento)
