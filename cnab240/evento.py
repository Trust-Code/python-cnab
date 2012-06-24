
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
