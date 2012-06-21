
import unittest
import errors

from registro import Registro
from decimal import Decimal

class TestRegistro(unittest.TestCase):
    
    def setUp(self):
        self.registro_str = (u'00100020         212345678901234abcdefghijklmn'
            u'opqrst028916000000014262X7TRACY TECNOLOGIA LTDA ME      BANCO '
            u'DO BRASIL                         0201207132200001234560851234'
            u'5                                                             '
            u'        ')
        self.registro = Registro('header_arquivo')
        self.registro.carregar(self.registro_str)
    
    def test_comprimento_de_registro(self):
        self.assertEqual(len(self.registro_str), 240)

    def test_leitura_campo_num_decimal(self):
        self.assertEqual(self.registro.controle_lote, Decimal('0.02'))  
    
    def test_escrita_campo_num_decimal(self):
        # aceitar somente tipo Decimal
        with self.assertRaises(errors.TipoError):
            self.registro.controle_lote = 10.0 
        with self.assertRaises(errors.TipoError):
            self.registro.controle_banco = '' 
       
        # Testa se as casas decimais estao sendo verificadas 
        with self.assertRaises(errors.NumDecimaisError): 
            self.registro.controle_lote = Decimal('100.2')
        with self.assertRaises(errors.NumDecimaisError): 
            self.registro.controle_lote = Decimal('1001')
        with self.assertRaises(errors.NumDecimaisError): 
            self.registro.controle_lote = Decimal('1.000')
       
        # verifica se o numero de digitos esta sendo verificado 
        with self.assertRaises(errors.NumDigitosExcedidoError): 
            self.registro.controle_lote = Decimal('100.21')
       
        # armazemamento correto de um decimal 
        self.registro.controle_lote = Decimal('2.13')
        self.assertEqual(self.registro.controle_lote, Decimal('2.13'))
    
    def test_leitura_campo_num_int(self):
        self.assertEqual(self.registro.controle_banco, 1)
    
    def test_escrita_campo_num_int(self):
        # aceitar somente inteiros (int e long)
        with self.assertRaises(errors.TipoError):
            self.registro.controle_banco = 10.0 
        with self.assertRaises(errors.TipoError):
            self.registro.controle_banco = '' 
       
        # verifica se o numero de digitos esta sendo verificado 
        with self.assertRaises(errors.NumDigitosExcedidoError): 
            self.registro.controle_banco = 12345678234567890234567890 
        with self.assertRaises(errors.NumDigitosExcedidoError): 
            self.registro.controle_banco = 1234
        
        # verifica valor armazenado 
        self.registro.controle_banco = 5
        self.assertEqual(self.registro.controle_banco, 5)
         
    def test_leitura_campo_alfa(self):
        self.assertEqual(self.registro.empresa_nome, 
                         u'TRACY TECNOLOGIA LTDA ME')
    
    def test_escrita_campo_alfa(self):
        # Testa que serao aceitos apenas unicode objects
        with self.assertRaises(errors.TipoError):
            self.registro.empresa_nome = 'tracy' 

        # Testa que strings mais longas que obj.digitos nao serao aceitas 
        with self.assertRaises(errors.NumDigitosExcedidoError):
            self.registro.empresa_convenio = u'123456789012345678901'
       
        # Testa que o valor atribuido foi guardado no objeto 
        self.registro.empresa_nome = u'tracy' 
        self.assertEqual(self.registro.empresa_nome, 'tracy')
     
if __name__ == '__main__':
    unittest.main()
