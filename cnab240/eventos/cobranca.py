
from cnab240.tipos import EventoBase


class EventoInclusao(EventoBase):
    def __init__(self, banco, **kwargs):
        super(EventoInclusao, self).__init__(banco, 1)
        args = self.clean_kwargs(kwargs)

        seg_p = self.banco.registros.SegmentoP(**args)
        self.adicionar_segmento(seg_p)

        seg_q = self.banco.registros.SegmentoQ(**args)
        self.adicionar_segmento(seg_q)

        seg_r = self.banco.registros.SegmentoR(**args)
        if seg_r.necessario():
            self.adicionar_segmento(seg_r)
