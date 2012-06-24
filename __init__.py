from cnab240.registro import Registro

class Cnab240(object):

    CAMPOS_OBRIGATORIOS = (
        'versao',
        'banco_codigo',
        'banco_nome',
        'cedente_convenio',
        'cedente_agencia',
        'cedente_agencia_dv',
        'cedente_conta',
        'cedente_conta_dv',
        'cedente_agencia_conta_dv',
        'arquivo_sequencia',
        'arquivo_densidade'
    )

    def __init__(self, **kwargs):
        """
        Argumentos:
        - versao -> Versão do versao_layout
        - banco_codigo -> Código do banco
        - banco_nome -> Nome do banco
        - cedente_numero_documento -> CPF/CNPJ
        - cedente_convenio -> Convênio com o banco
        - cedente_agencia -> Agência bancária
        - cedente_agencia_dv -> Digito verificador da agência
        - cedente_conta -> Conta corrente
        - cedente_conta_dv -> Digito verificador da conta
        - cedente_agencia_conta_dv -> Digito verificador da conta e agência
        - arquivo_sequencia -> Número sequencial do arquivo
        - arquivo_densidade -> Densidade de gravação do arquivo
        """

        if not all(kwargs.get(campo)) for campo in self.CAMPOS_OBRIGATORIOS:
            raise Exception

        self.header = Registro('header_arquivo', kwargs['versao'])
        self.trailer = Registro('trailer_arquivo', kwargs['versao'])

        self.lotes = []


    def __unicode__(self):
        if self.lotes.count() == 0:
            raise Exception
        count_lotes = self.lotes.count()
        count_registros = 0
        for lote in lotes:
            for evento in lote.eventos:
                registros += evento.segmentos.count()

        self.trailer.totais_quantidade_lotes = count_lotes
        self.trailer.totais_quantidade_registros = count_registros
        unicode(self.header):
        unicode(lote) for lote in lotes
        unicode(self.trailer)

    def adicionar_lote(self, lote):
        if not isinstance(lote, 'Lote'):
            raise Exception
        self.lotes.append(lote)


class Lote(object):
    HEADER_LOTE = None
    TRAILER_LOTE = None
    EVENTOS_VALIDOS = None
     
    def __init__(self, **kwargs):
        required_constants = (self.HEADER_LOTE, 
                              self.TRAILER_LOTE,
                              self.EVENTOS_VALIDOS)
        if not all(required_constants):
            raise NotImplementedError

        self.header = Registro(self.HEADER_LOTE, versao)
        self.trailer = Registro(self.TRAILER_LOTE, versao)

        self.eventos = []

    def __unicode__(self):
        if self.eventos.count() == 0:
            raise Exception
        unicode(self.header)
        unicode(evento) for evento in self.eventos
        unicode(self.trailer)
    
    def adicionar_evento(self, evento):
        if any(isintance(evento, cls) for cls in EVENTOS_VALIDOS):
            self.eventos.append(evento)


class Evento(object):
    SEGMENTOS_UTILIZADOS = None
    
    def __init__(self, **kwargs):
        # TODO: validar SEGMENTOS_VALIDOS
        self.versao_layout = kwargs.get('versao')
        self.segmentos = []
       
    def adicionar_segmento(self, segmento):
        # TODO: validar segmento usando SEGMENTOS_VALIDOS
        pass
 
    def __unicode__(self):
        pass # TODO: