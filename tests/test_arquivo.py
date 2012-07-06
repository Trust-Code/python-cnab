
import unittest

from cnab240 import errors
from cnab240.bancos import itau
from cnab240.tipos import Arquivo
from tests.data import get_itau_data_from_file


class TestCnab240(unittest.TestCase):

    def setUp(self):
        self.itau_data = get_itau_data_from_file()
        arquivo_args = self.itau_data['header_arquivo'].todict().items()
        arquivo_args += self.itau_data['header_arquivo'].todict().items()
        self.arquivo = Arquivo(itau, **dict(arquivo_args))

    def test_unicode(self):
        args_evento1 = self.itau_data['seg_p1'].todict().items()
        args_evento1 += self.itau_data['seg_q1'].todict().items()
        self.arquivo.incluir_cobranca(**dict(args_evento1))

    def test_empty_data(self):
        arquivo = Arquivo(itau)
        self.assertRaises(errors.ArquivoVazioError, unicode, arquivo)

if __name__ == '__main__':
    unittest.main()
