from cnab240.bancos import bb
from cnab240.tipos import ArquivoBase, LoteBase, EventoBase


class Arquivo(ArquivoBase):
    banco = bb

class Lote(LoteBase):
    pass

class Evento(EventoBase):
    pass