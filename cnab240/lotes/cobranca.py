
from cnab240.tipos import LoteBase


class LoteCobranca(LoteBase):
    HeaderCls = LoteCobranca.banco.registros.HeaderLoteCobranca
    TrailerCls = LoteCobranca.banco.registros.TrailerLoteCobranca
