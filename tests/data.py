
import os
import codecs
from cnab240.bancos import itau
from cnab240.tipos import Lote, Evento

TESTS_DIRPATH = os.path.abspath(os.path.dirname(__file__))
ARQS_DIRPATH = os.path.join(TESTS_DIRPATH, 'arquivos')

def get_itau_data():
    itau_data = dict()
    arquivo_remessa = codecs.open(os.path.join(ARQS_DIRPATH, 
                                     'cobranca.itau.rem'), encoding='ascii')

    itau_data['remessa'] = arquivo_remessa.read()
    arquivo_remessa.seek(0)

    itau_data['header_arquivo'] = itau.registros.HeaderArquivo()
    itau_data['header_arquivo_str'] = arquivo_remessa.readline().strip('\r\n')
    itau_data['header_arquivo'].carregar(itau_data['header_arquivo_str'])

    itau_data['header_lote'] = itau.registros.HeaderLoteCobranca()
    itau_data['header_lote_str'] = arquivo_remessa.readline().strip('\r\n')
    itau_data['header_lote'].carregar(itau_data['header_lote_str'])

    itau_data['seg_p1'] = itau.registros.SegmentoP()
    itau_data['seg_p1_str'] = arquivo_remessa.readline().strip('\r\n')
    itau_data['seg_p1'].carregar(itau_data['seg_p1_str'])

    itau_data['seg_q1'] = itau.registros.SegmentoQ()
    itau_data['seg_q1_str'] = arquivo_remessa.readline().strip('\r\n')
    itau_data['seg_q1'].carregar(itau_data['seg_q1_str'])

    itau_data['seg_p2'] = itau.registros.SegmentoP()
    itau_data['seg_p2_str'] = arquivo_remessa.readline().strip('\r\n')
    itau_data['seg_p2'].carregar(itau_data['seg_p2_str'])

    itau_data['seg_q2'] = itau.registros.SegmentoQ()
    itau_data['seg_q2_str'] = arquivo_remessa.readline().strip('\r\n')
    itau_data['seg_q2'].carregar(itau_data['seg_q2_str'])

    itau_data['trailer_lote'] = itau.registros.TrailerLoteCobranca()
    itau_data['trailer_lote_str'] = arquivo_remessa.readline().strip('\r\n')
    itau_data['trailer_lote'].carregar(itau_data['trailer_lote_str'])

    itau_data['trailer_arquivo'] = itau.registros.TrailerArquivo()
    itau_data['trailer_arquivo_str'] = arquivo_remessa.readline().strip('\r\n')
    itau_data['trailer_arquivo'].carregar(itau_data['trailer_arquivo_str'])

    itau_data['lote_cob'] = Lote(itau, itau_data['header_lote'],
                                                    itau_data['trailer_lote'])
    itau_data['evento_cob1'] = Evento(itau, 1)
    itau_data['evento_cob1'].adicionar_segmento(itau_data['seg_p1'])
    itau_data['evento_cob1'].adicionar_segmento(itau_data['seg_q1'])

    itau_data['evento_cob2'] = Evento(itau, 1)
    itau_data['evento_cob2'].adicionar_segmento(itau_data['seg_p2'])
    itau_data['evento_cob2'].adicionar_segmento(itau_data['seg_q2'])
   
    arquivo_remessa.close() 
    return itau_data
