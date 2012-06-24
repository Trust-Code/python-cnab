
import unittest

from cnab240 import errors
from cnab240.lote import Lote
from cnab240.registro import Registro 
from tests.data import REGISTRO_T, EventoImplementado, LoteImplementado

class TestLote(unittest.TestCase):

    def test_lote_invalido(self):
        with self.assertRaises(NotImplementedError):
            lote = Lote(versao='085')

    def test_adicionar_evento_invalido(self):
        lote = LoteImplementado(versao='085')
        with self.assertRaises(TypeError):
            lote.adicionar_evento('evento')

    def test_adicionar_evento(self):
        registro = Registro('segmento_t', '085')
        registro.carregar(REGISTRO_T)
        evento = EventoImplementado(versao='085')
        evento.adicionar_segmento(registro) 
        lote = LoteImplementado(versao='085')
        lote.adicionar_evento(evento)
        
        self.assertEqual(lote._eventos[0], evento)
        
        evento2 = EventoImplementado(versao='085')
        self.assertNotEqual(lote._eventos[0], evento2)
    
if __name__ == '__main__':
    unittest.main()
