
import unittest

from cnab240 import errors
from cnab240.bancos import itau
from cnab240.lotes.cobranca import LoteCobranca 
from cnab240.eventos.cobranca import EventoInclusao


class TestLote(unittest.TestCase):

    def setUp(self):
        self.lote_itau = LoteCobranca(itau)
        self.inclusao = EventoInclusao(itau) 

    def test_init(self):
        self.assertEqual(self.lote_itau.eventos, []) 
        self.assertEqual(self.lote_itau.trailer.quantidade_registros, 2) 
   
    def test_adicionar_evento(self):
        with self.assertRaises(TypeError):
            self.lote_itau.adicionar_evento(None)

        self.lote_itau.adicionar_evento(self.inclusao)
        self.assertEqual(self.lote_itau.trailer.quantidade_registros, 4)
        
        self.lote_itau.adicionar_evento(self.inclusao)
        self.assertEqual(self.lote_itau.trailer.quantidade_registros, 6)
    
    def test_unicode(self):
        with self.assertRaises(errors.NenhumEventoError):
            unicode(self.lote_itau)
    
    def test_definir_codigo(self):
        self.lote_itau.adicionar_evento(self.inclusao)
        self.lote_itau.codigo = 129 

        self.assertEqual(self.lote_itau.header.controle_lote, 129)
        self.assertEqual(self.lote_itau.trailer.controle_lote, 129)
        for evento in self.lote_itau.eventos:
            for seg in evento.segmentos:
                self.assertEqual(seg.controle_lote, 129)
    
    
