
import unittest

from unittest import skip

from decimal import Decimal
from cnab240 import errors
from cnab240.bancos import itau
from tests.data import get_itau_data_from_file


class TestRegistro(unittest.TestCase):

    def setUp(self):
        itau_data = get_itau_data_from_file()
        self.header_arquivo = itau_data['header_arquivo']
        self.seg_p = itau_data['seg_p1']
        self.seg_p_str = itau_data['seg_p1_str']
        self.seg_q = itau_data['seg_q1']
        self.seg_q_str = itau_data['seg_q1_str']

    def test_leitura_campo_num_decimal(self):
        self.assertEqual(self.seg_p.valor_titulo, Decimal('100.00'))

    def test_escrita_campo_num_decimal(self):
        # aceitar somente tipo Decimal
        with self.assertRaises(errors.TipoError):
            self.seg_p.valor_titulo = 10.0
        with self.assertRaises(errors.TipoError):
            self.seg_p.valor_titulo = ''

        # Testa se as casas decimais estao sendo verificadas
        with self.assertRaises(errors.NumDecimaisError):
            self.seg_p.valor_titulo = Decimal('100.2')
        with self.assertRaises(errors.NumDecimaisError):
            self.seg_p.valor_titulo = Decimal('1001')
        with self.assertRaises(errors.NumDecimaisError):
            self.seg_p.valor_titulo = Decimal('1.000')

        # verifica se o numero de digitos esta sendo verificado
        with self.assertRaises(errors.NumDigitosExcedidoError):
            self.seg_p.valor_titulo = Decimal('10000000008100.21')

        # armazemamento correto de um decimal
        self.seg_p.valor_titulo = Decimal('2.13')
        self.assertEqual(self.seg_p.valor_titulo, Decimal('2.13'))

    def test_leitura_campo_num_int(self):
        self.assertEqual(self.header_arquivo.controle_banco, 341)

    def test_escrita_campo_num_int(self):
        # aceitar somente inteiros (int e long)
        with self.assertRaises(errors.TipoError):
            self.header_arquivo.controle_banco = 10.0
        with self.assertRaises(errors.TipoError):
            self.header_arquivo.controle_banco = ''

        # verifica se o numero de digitos esta sendo verificado
        with self.assertRaises(errors.NumDigitosExcedidoError):
            self.header_arquivo.controle_banco = 12345678234567890234567890
        with self.assertRaises(errors.NumDigitosExcedidoError):
            self.header_arquivo.controle_banco = 1234

        # verifica valor armazenado
        self.header_arquivo.controle_banco = 5
        self.assertEqual(self.header_arquivo.controle_banco, 5)

    def test_leitura_campo_alfa(self):
        self.assertEqual(self.header_arquivo.cedente_nome,
                         'TRACY TECNOLOGIA LTDA ME')

    @skip
    def test_escrita_campo_alfa(self):
        # Testa que serao aceitos apenas unicode objects
        with self.assertRaises(errors.TipoError):
            self.header_arquivo.cedente_nome = 'tracy'

        # Testa que strings mais longas que obj.digitos nao serao aceitas
        with self.assertRaises(errors.NumDigitosExcedidoError):
            self.header_arquivo.cedente_convenio = '123456789012345678901'

        # Testa que o valor atribuido foi guardado no objeto
        self.header_arquivo.cedente_nome = 'tracy'
        self.assertEqual(self.header_arquivo.cedente_nome, 'tracy')

    def test_fromdict(self):
        header_dict = self.header_arquivo.todict()
        header_arquivo = itau.registros.HeaderArquivo(**header_dict)
        self.assertEqual(header_arquivo.cedente_nome,
                                                'TRACY TECNOLOGIA LTDA ME')
        self.assertEqual(header_arquivo.nome_do_banco, 'BANCO ITAU SA')

    def test_necessario(self):
        self.assertTrue(self.seg_p)

        seg_p2 = itau.registros.SegmentoP()
        self.assertFalse(seg_p2.necessario())

        seg_p2.controle_banco = 33
        self.assertFalse(seg_p2.necessario())

        seg_p2.vencimento_titulo = 10102012
        self.assertTrue(seg_p2.necessario())

    def test_unicode(self):
        def unicode_test(seg_instance, seg_str):
            seg_gen_str = str(seg_instance)

            self.assertEqual(len(seg_gen_str), 240)
            self.assertEqual(len(seg_str), 240)
            self.assertEqual(seg_gen_str, seg_str)

        unicode_test(self.seg_p, self.seg_p_str)
        unicode_test(self.seg_q, self.seg_q_str)

if __name__ == '__main__':
    unittest.main()
