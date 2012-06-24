
from cnab240 import errors
from cnab240.registro import Registro


class Lote(object):

    REQUIRED_CONSTANTS = {
        'header_lote': None,
        'trailer_lote': None,
        'eventos_validos': None,
    }    
 
    def __init__(self, **kwargs):
        if not all(self.REQUIRED_CONSTANTS.values()):
            raise NotImplementedError

        header_lote = self.REQUIRED_CONSTANTS.get('header_lote')
        trailer_lote = self.REQUIRED_CONSTANTS.get('trailer_lote')
        versao = kwargs.get('versao')       
 
        self.header = Registro(header_lote, versao)
        self.trailer = Registro(header_lote, versao)

        self._eventos = []
    
    def adicionar_evento(self, evento):
        eventos_validos = self.REQUIRED_CONSTANTS.get('eventos_validos')
        if any(isinstance(evento, cls) for cls in eventos_validos):
            self._eventos.append(evento)
        else:
            raise TypeError

    def __unicode__(self):
        if not self._eventos:
            errors.NenhumEventoError()
    
        result = [] 
        result.append(unicode(self.header))
        result.extend(unicode(evento) for evento in self._eventos)
        result.append(unicode(self.trailer))
        return '\n'.join(result)
