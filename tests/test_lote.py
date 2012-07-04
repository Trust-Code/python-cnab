
import os
import codecs
import unittest

from cnab240 import errors
from cnab240.bancos import itau
from cnab240.tipos import Lote 
from cnab240.eventos.cobranca import EventoInclusao
from tests.data import HEADER_COB_ITAU_DICT, TRAILER_COB_ITAU_DICT, \
                                ARQS_DIRPATH, SEG_P_ITAU_DICT, SEG_Q_ITAU_DICT

class TestLote(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestLote, self).__init__(*args, **kwargs)
        self.maxDiff = None        

    def setUp(self):
        rem_itau_path = os.path.join(ARQS_DIRPATH, 'cobranca.itau.rem')
        self.arquivo_itau = codecs.open(rem_itau_path, encoding='ascii') 
        
        self.arquivo_itau.readline() # Ignorando o header do arquivo
        self.header_cob_itau_str = self.arquivo_itau.readline().strip()
        self.seg_p_1_str = self.arquivo_itau.readline().strip()
        self.seg_q_1_str = self.arquivo_itau.readline().strip()
        self.seg_p_2_str = self.arquivo_itau.readline().strip()
        self.seg_q_2_str = self.arquivo_itau.readline().strip()
        self.trailer_cob_itau_str = self.arquivo_itau.readline().strip() 
        
        header_lote = itau.registros.HeaderLoteCobranca()
        header_lote.carregar(self.header_cob_itau_str)

        trailer_lote = itau.registros.TrailerLoteCobranca()
        trailer_lote.carregar(self.trailer_cob_itau_str)

        seg_p_1 = itau.registros.SegmentoP()
        seg_p_1.carregar(self.seg_p_1_str)
        seg_p_1_dict = seg_p_1.todict()

        seg_q_1 = itau.registros.SegmentoQ()
        seg_q_1.carregar(self.seg_q_1_str)
        seg_q_1_dict = seg_q_1.todict()

        seg_p_2 = itau.registros.SegmentoP()
        seg_p_2.carregar(self.seg_p_2_str)
        seg_p_2_dict = seg_p_2.todict()

        seg_q_2 = itau.registros.SegmentoQ()
        seg_q_2.carregar(self.seg_q_2_str)
        seg_q_2_dict = seg_q_2.todict()

        self.lote_itau = Lote(itau, header_lote, trailer_lote)
         
        args_evento_1 = dict(seg_p_1_dict.items() + seg_q_1_dict.items())
        args_evento_2 = dict(seg_p_2_dict.items() + seg_q_2_dict.items())

        self.evento_1 = EventoInclusao(itau, **args_evento_1) 
        self.evento_2 = EventoInclusao(itau, **args_evento_2) 
        
        self.arquivo_itau.seek(0)
    
    def test_init(self):
        self.assertEqual(self.lote_itau.eventos, []) 
        self.assertEqual(self.lote_itau.trailer.quantidade_registros, 2) 
   
    def test_adicionar_evento(self):
        with self.assertRaises(TypeError):
            self.lote_itau.adicionar_evento(None)

        self.lote_itau.adicionar_evento(self.evento_1)
        self.assertEqual(self.lote_itau.trailer.quantidade_registros, 4)
        
        self.lote_itau.adicionar_evento(self.evento_2)
        self.assertEqual(self.lote_itau.trailer.quantidade_registros, 6)
    
    def test_unicode(self):
        with self.assertRaises(errors.NenhumEventoError):
            unicode(self.lote_itau)
    
        self.lote_itau.adicionar_evento(self.evento_1)
        self.lote_itau.adicionar_evento(self.evento_2)
        self.lote_itau.codigo = 1
   
        arquivo_itau_lines = self.arquivo_itau.readlines() 
        lote_lines = arquivo_itau_lines[1:-1] 
        lote_str = u''.join(lote_lines).strip('\r\n')

        self.assertEqual(unicode(self.lote_itau), lote_str)
        
    def test_definir_codigo(self):
        self.lote_itau.adicionar_evento(self.evento_1)
        self.lote_itau.codigo = 129

        self.assertEqual(self.lote_itau.header.controle_lote, 129)
        self.assertEqual(self.lote_itau.trailer.controle_lote, 129)
        for evento in self.lote_itau.eventos:
            for seg in evento.segmentos:
                self.assertEqual(seg.controle_lote, 129)
 
