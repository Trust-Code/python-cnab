# -*- coding: utf-8 -*-

from cnab240.registro import Registro
from datetime import datetime

class Cnab240(object):

    CAMPOS_OBRIGATORIOS = (
        'versao',
        'banco_codigo',
        'banco_nome',
        'cedente_nome',
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
        - cedente_banco_codigo -> Código do banco
        - cedente_banco_nome -> Nome do banco
        - cedente_nome -> Nome do Cedente
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

        if not all(kwargs.has_key(campo) for campo in self.CAMPOS_OBRIGATORIOS):
            #TODO: raise right exception
            raise Exception

        self.header = Registro('header_arquivo', kwargs.get('versao'))
        self.trailer = Registro('trailer_arquivo', kwargs.get('versao'))

        # HEADER

        # 01.0
        self.header.controle_banco = kwargs.get('cedente_banco_codigo')

        # 05.0
        # CPF
        if len(kwargs.get('cedente_numero_documento')) == 11:
            self.header.empresa_inscricao_tipo = 1
        # CNPJ
        elif len(kwargs.get('cedente_numero_documento')) == 14:
            self.header.empresa_inscricao_tipo = 2
        # Documento inválido
        else:
            raise Exception # TODO
        # 06.0 
        self.header.empresa_inscricao_numero = kwargs.get('cedente_numero_documento')
        # 07.0
        self.header.empresa_convenio = kwargs.get('cedente_convenio')
        # 08.0
        self.header.empresa_conta_agencia_codigo = kwargs.get('cedente_agencia')
        # 09.0
        self.header.empresa_conta_agencia_dv = kwargs.get('cedente_agencia_dv')
        # 10.0
        self.header.empresa_conta_numero = kwargs.get('cedente_conta')
        # 11.0
        self.header.empresa_conta_dv = kwargs.get('cedente_conta_dv')
        # 12.0
        self.header.empresa_agencia_conta_dv = kwargs.get('cedente_agencia_conta_dv')
        # 13.0
        self.header.empresa_nome = kwargs.get('cedente_nome')
        # 14.0
        self.header.nome_do_banco = kwargs.get('cedente_banco_nome')

        # 16.0
        # 1 -> Remessa; 2 -> Retorno
        self.header.arquivo_codigo = 1

        now = datetime.now()
        # 17.0
        self.header.arquivo_data_de_geracao = now.strftime("%d%m%y")
        # 18.0
        self.header.arquivo_hora_de_geracao = now.strftime("%H%M%S")
        # 19.0
        self.header.arquivo_sequencia = kwargs.get('arquivo_sequencia')
        # 21.0
        self.header.arquivo_densidade = kwargs.get('arquivo_densidade')

        # TRAILER
        # 01.9
        self.trailer.controle_banco = kwargs.get('cedente_banco_codigo')
        # 05.9
        self.trailer.totais_quantidade_lotes = 0
        # 06.9
        self.trailer.totais_quantidade_registros = 0
        # 07.9
        self.lotes = []

    def __unicode__(self):
        if self.lotes.count() == 0:
            raise Exception # TODO
        
        result = []
        result.append(unicode(self.header))
        result.extend(unicode(lote) for lote in self.lotes)
        result.append(unicode(self.trailer))
        return '\n'.join(result)
        
    def adicionar_lote(self, lote):
        if not isinstance(lote, 'Lote'):
            raise Exception # TODO
        self.lotes.append(lote)

        # Incrementar numero de lotes no trailer do arquivo
        self.trailer.totais_quantidade_lotes += 1

        # Incrementar numero de registros no trailer do arquivo
        for evento in lote.eventos:
            self.trailer.totais_quantidade_registros += evento.segmentos.count()

    def escrever(self, file_):
        file_.write(unicode(self.header))
        file_.write('\n')
        for lote in self.lotes:
            file_.write(unicode(lote))
            file_.write('\n')
        file_.write(unicode(self.trailer))
        file_.write('\n')


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
            raise Exception # TODO: raise exception
    
        result = [] 
        result.append(unicode(self.header))
        result.extend(unicode(evento) for evento in self.eventos)
        result.append(unicode(self.trailer))
        return '\n'.join(result)
    
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
