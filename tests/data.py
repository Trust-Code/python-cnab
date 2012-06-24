
from cnab240.evento import Evento
from cnab240.lote import Lote

HEADER_ARQUIVO_STR = u'00100020         212345678901234abcdefghijklmnopqrst028916000000014262X7TRACY TECNOLOGIA LTDA ME      BANCO DO BRASIL                         02012071322000012345608512345                                                                     '

REGISTRO_T = u'0336774300001T 1702260800001300040110000000000000000000601               04082011000000000004350001000308                         002000000000000000                                        01300040110000000000002640400000000                 '

class EventoImplementado(Evento):
    SEGMENTOS_VALIDOS = ('T', 'U')

class LoteImplementado(Lote):
    REQUIRED_CONSTANTS = {
        'header_lote': 'header_lote_cobranca',
        'trailer_lote': 'trailer_lote_cobranca',
        'eventos_validos': (EventoImplementado, )
    }
