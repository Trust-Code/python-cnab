
import unittest

from cnab240 import errors
from cnab240.bancos.bb.tipos import Arquivo


class TestCnab240(unittest.TestCase):

    def setUp(self):
        self.arquivo_bb = Arquivo()
        
    def test_nenhum_lote(self):
        with self.assertRaises(errors.ArquivoVazioError):
            unicode(self.arquivo_bb)

    def test_erro_de_lote(self):
        with self.assertRaises(TypeError):
            self.arquivo_bb.adicionar_lote('Lote')


if __name__ == '__main__':
    unittest.main()
