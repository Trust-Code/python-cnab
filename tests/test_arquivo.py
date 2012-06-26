
import unittest

from cnab240 import errors
from cnab240.bancos.bb.tipos import Arquivo


class TestCnab240(unittest.TestCase):

    def setUp(self):
        self.args = {
            'versao': u'085',
            'cedente_banco_codigo': 1,
            'cedente_banco_nome': u'Banco do Brasil',
            'cedente_nome': u'Tracy Web',
            'cedente_convenio': u'abcdefghijklm',
            'cedente_agencia': 323,
            'cedente_agencia_dv': u'9',
            'cedente_conta': 233,
            'cedente_conta_dv': u'X',
            'cedente_agencia_conta_dv': u'P',
            'cedente_numero_documento': 12345678900,
            'arquivo_sequencia': 1,
            'arquivo_densidade': 324,
        }

        self.arquivo_bb = Arquivo()
        
    def test_nenhum_lote(self):
        with self.assertRaises(errors.ArquivoVazioError):
            unicode(self.arquivo_bb)

    def test_erro_de_lote(self):
        with self.assertRaises(TypeError):
            self.arquivo_bb.adicionar_lote('Lote')


if __name__ == '__main__':
    unittest.main()
