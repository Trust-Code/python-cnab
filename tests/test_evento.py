
import unittest
from cnab240.bancos import itau
from cnab240.tipos import Evento
from tests.data import get_itau_data_from_file

class TestEvento(unittest.TestCase):
    def setUp(self):
        self.evento = Evento(itau, 1)
   
    def test_getattributes(self):
        self.assertEquals(self.evento._segmentos, [])

        test_obj = type('TestObject', (object,), {'test_attr': None})()
        self.evento._segmentos.append(test_obj)
        test_obj.test_attr = 'Hello World'
        self.evento.test_attr = 'Goodbye World'

        self.assertNotEqual(self.evento.test_attr, 'Goodbye World')
        self.assertEqual(self.evento.test_attr, 'Hello World')

    def test_unicode(self):  
        self.assertEquals(unicode(self.evento), u'')
        self.evento._segmentos.append('test_1')
        self.assertEquals(unicode(self.evento), u'test_1') 
        self.evento._segmentos.append('test_2') 
        self.assertEquals(unicode(self.evento), u'test_1\r\ntest_2') 

