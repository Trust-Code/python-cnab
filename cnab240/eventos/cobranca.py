
from cnab240.tipos import EventoBase


class EventoInclusao(EventoBase):
    def __init__(self, banco, **kwargs):
        super(EventoInclusao, self).__init__(banco)
        seg_p = self.banco.registros.SegmentoP(**kwargs)
        self._segmentos.append(seg_p)
 
        seg_q = self.banco.registros.SegmentoQ(**kwargs)
        self._segmentos.append(seg_q)

        seg_r = self.banco.registros.SegmentoR(**kwargs)
        if seg_r.necessario():  
            self._segmentos.append(seg_r) 
