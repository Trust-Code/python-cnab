
import unittest

from decimal import Decimal
from cnab240 import errors
from cnab240.bancos import bb
from tests.data import HEADER_ARQUIVO_STR, REGISTRO_T



class TestRegistro(unittest.TestCase):
    
    def setUp(self):
        self.header_arquivo = bb.registros.HeaderArquivo()
        self.header_arquivo.carregar(HEADER_ARQUIVO_STR)
        
        self.seg_t = bb.registros.SegmentoT()
        self.seg_t.carregar(REGISTRO_T)

    def test_leitura_campo_num_decimal(self):
        self.assertEqual(self.seg_t.valor_titulo, Decimal('43.50'))  
    
    def test_escrita_campo_num_decimal(self):
        # aceitar somente tipo Decimal
        with self.assertRaises(errors.TipoError):
            self.seg_t.valor_titulo = 10.0 
        with self.assertRaises(errors.TipoError):
            self.seg_t.valor_titulo = '' 
       
        # Testa se as casas decimais estao sendo verificadas 
        with self.assertRaises(errors.NumDecimaisError): 
            self.seg_t.valor_titulo = Decimal('100.2')
        with self.assertRaises(errors.NumDecimaisError): 
            self.seg_t.valor_titulo = Decimal('1001')
        with self.assertRaises(errors.NumDecimaisError): 
            self.seg_t.valor_titulo = Decimal('1.000')
       
        # verifica se o numero de digitos esta sendo verificado 
        with self.assertRaises(errors.NumDigitosExcedidoError): 
            self.seg_t.valor_titulo = Decimal('10000000008100.21')
       
        # armazemamento correto de um decimal 
        self.seg_t.valor_titulo = Decimal('2.13')
        self.assertEqual(self.seg_t.valor_titulo, Decimal('2.13'))
    
    def test_leitura_campo_num_int(self):
        self.assertEqual(self.header_arquivo.controle_banco, 1)
    
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
        self.assertEqual(self.header_arquivo.empresa_nome, 
                         u'TRACY TECNOLOGIA LTDA ME')
    
    def test_escrita_campo_alfa(self):
        # Testa que serao aceitos apenas unicode objects
        with self.assertRaises(errors.TipoError):
            self.header_arquivo.empresa_nome = 'tracy' 

        # Testa que strings mais longas que obj.digitos nao serao aceitas 
        with self.assertRaises(errors.NumDigitosExcedidoError):
            self.header_arquivo.empresa_convenio = u'123456789012345678901'
       
        # Testa que o valor atribuido foi guardado no objeto 
        self.header_arquivo.empresa_nome = u'tracy' 
        self.assertEqual(self.header_arquivo.empresa_nome, 'tracy')
     
if __name__ == '__main__':
    unittest.main()
