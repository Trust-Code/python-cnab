
import unittest

from cnab240 import Cnab240
from cnab240 import errors


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

        self.cnab240 = Cnab240(**self.args)
    
    def test_faltando_args(self):
        args = dict(self.args.items())
        del args['arquivo_sequencia'] 
        with self.assertRaises(errors.FaltandoArgsError):
            cnab240 = Cnab240(**args)

if __name__ == '__main__':
    unittest.main()
