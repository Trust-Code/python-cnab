
try:
    import unittest2 as unittest
except ImportError:
    import unittest

from cnab240.bancos import itau
from cnab240.tipos import Evento


class TestEvento(unittest.TestCase):
    def setUp(self):
        self.evento = Evento(itau, 1)

    def test_getattributes(self):
        self.assertEqual(self.evento._segmentos, [])

        test_obj = type('TestObject', (object,), {'test_attr': None})()
        self.evento._segmentos.append(test_obj)
        test_obj.test_attr = 'Hello World'
        self.evento.test_attr = 'Goodbye World'

        self.assertNotEqual(self.evento.test_attr, 'Goodbye World')
        self.assertEqual(self.evento.test_attr, 'Hello World')

    def test_unicode(self):
        self.assertEqual(str(self.evento), '')
        self.evento._segmentos.append('test_1')
        self.assertEqual(str(self.evento), 'test_1')
        self.evento._segmentos.append('test_2')
        self.assertEqual(str(self.evento), 'test_1\r\ntest_2')
