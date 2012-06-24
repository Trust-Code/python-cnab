
import unittest

from cnab240.evento import Evento
from cnab240.registro import Registro
from tests.data import REGISTRO_T, EventoImplementado


class TestEvento(unittest.TestCase):
    
    def test_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            evento = Evento(versao='085')

    def test_segmento_invalido(self):
        evento = EventoImplementado(versao='085') 
        with self.assertRaises(TypeError):
            evento.adicionar_segmento('evento')

    def test_segmento_valido(self):
        evento = EventoImplementado(versao='085') 
        registro = Registro('segmento_t', '085')
        registro.carregar(REGISTRO_T) 
        evento.adicionar_segmento(registro)
        self.assertEqual(evento._segmentos['T'], registro)
