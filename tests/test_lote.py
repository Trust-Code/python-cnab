
try:
    import unittest2 as unittest
except ImportError:
    import unittest

import os
import codecs

from cnab240 import errors
from cnab240.bancos import itau
from cnab240.tipos import Lote
from tests.data import get_itau_data_from_file


class TestLote(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestLote, self).__init__(*args, **kwargs)
        self.maxDiff = None

    def setUp(self):
        itau_data = get_itau_data_from_file()
        self.lote = itau_data['lote_cob']
        self.evento_1 = itau_data['evento_cob1']
        self.evento_2 = itau_data['evento_cob2']
        self.remessa = itau_data['remessa']

    def test_init(self):
        self.assertEqual(self.lote.eventos, [])
        self.assertEqual(self.lote.trailer.quantidade_registros, 2)

    def test_adicionar_evento(self):
        with self.assertRaises(TypeError):
            self.lote.adicionar_evento(None)

        self.lote.adicionar_evento(self.evento_1)
        self.assertEqual(self.lote.trailer.quantidade_registros, 4)

        self.lote.adicionar_evento(self.evento_2)
        self.assertEqual(self.lote.trailer.quantidade_registros, 6)

    def test_unicode(self):
        with self.assertRaises(errors.NenhumEventoError):
            unicode(self.lote)

        self.lote.adicionar_evento(self.evento_1)
        self.lote.adicionar_evento(self.evento_2)
        self.lote.codigo = 1

        self.assertIn(unicode(self.lote), self.remessa)

    def test_definir_codigo(self):
        self.lote.adicionar_evento(self.evento_1)
        self.lote.codigo = 129

        self.assertEqual(self.lote.header.controle_lote, 129)
        self.assertEqual(self.lote.trailer.controle_lote, 129)
        for evento in self.lote.eventos:
            for seg in evento.segmentos:
                self.assertEqual(seg.controle_lote, 129)
