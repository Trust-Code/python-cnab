
from cnab240.tipos import LoteBase

class LoteCobranca(LoteBase):

    def __init__(self, banco):
        header = banco.registros.HeaderLoteCobranca() 
        trailer = banco.registros.TrailerLoteCobranca() 
        super(LoteCobranca, self).__init__(banco, header, trailer) 

