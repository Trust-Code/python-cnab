
import os
from cnab240.bancos.base.banco import Banco


class BancoDoBrasil(Banco):
    ALIAS = 'bb'
    SPECS_DIRPATH = os.path.join(os.path.abspath(
                                 os.path.dirname(__file__)), 'specs')
