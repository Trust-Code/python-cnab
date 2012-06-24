from cnab240.registro import Registro

class Cnab240(object):

    def __init__(self, **kwargs):
        self.lotes = None
        versao_layout = kwargs.get('versao')
        if not versao_layout:
            raise Exception

        self.header = Registro('header_arquivo', self.versao_layout)
        self.trailer = Registro('trailer_arquivo', self.versao_layout)

        

    def __unicode__(self):
        if not self._lotes:
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
        self._lotes.append(lote)