# -*- encoding: utf8 -*-

from datetime import datetime
from cnab240 import errors


class ArquivoBase(object):

    banco = None

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
        """ # TODO: Formatar docstrings em formato sphinx

        self.header = self.banco.registros.HeaderArquivo()
        self.header.fromdict(kwargs)
        
        self.trailer = self.banco.registros.TrailerArquivo()
        self.trailer.fromdict(kwargs)        
        
        self._lotes = []

    @property
    def lotes(self):
        return lotes

    def __unicode__(self):
        if not self._lotes:
            raise errors.ArquivoVazioError()
        
        result = []
        result.append(unicode(self.header))
        result.extend(unicode(lote) for lote in self._lotes)
        result.append(unicode(self.trailer))
        return u'\n'.join(result)
        
    def adicionar_lote(self, lote):
        if not isinstance(lote, 'Lote'):
            raise TypeError('Objeto deve ser instancia de "Lote"')
        self._lotes.append(lote)

        # Incrementar numero de lotes no trailer do arquivo
        self.trailer.totais_quantidade_lotes += 1

        # Incrementar numero de registros no trailer do arquivo
        for evento in lote.eventos:
            self.trailer.totais_quantidade_registros += evento.segmentos.count()

    def escrever(self, file_):
        file_.write(unicode(self.header))
        file_.write('\n')
        for lote in self._lotes:
            file_.write(unicode(lote))
            file_.write('\n')
        file_.write(unicode(self.trailer))
        file_.write('\n')


class EventoBase(object):
    segmentos_validos = {} 

    def __init__(self, **kwargs):
        if not self.segmentos_validos:
            raise NotImplementedError

        self._segmentos = dict.fromkeys(self.segmentos_validos.keys())
       
    def adicionar_segmento(self, segmento):
    
        if not isinstance(segmento, self.segmentos_validos.values()):
            raise TypeError

        self._segmentos.update({segmento.servico_segmento: segmento})

    @property
    def segmentos(self):    
        return self._segmentos
        
    def __unicode__(self):
        return u'\n'.join(unicode(seg) for seg in self._segmentos.values()
                          if seg) 


class LoteBase(object):

    banco = None
    eventos_validos = None
 
    def __init__(self):
        if not all(self.REQUIRED_CONSTANTS.values()):
            raise NotImplementedError

        self.header = self.banco.HeaderLote()
        self.trailer = self.banco.TrailerLote()
        self._eventos = []
    
    def adicionar_evento(self, evento):
        if any(isinstance(evento, cls) for cls in self.eventos_validos):
            self._eventos.append(evento)
        else:
            raise TypeError

    def __unicode__(self):
        if not self._eventos:
            errors.NenhumEventoError()
    
        result = [] 
        result.append(unicode(self.header))
        result.extend(unicode(evento) for evento in self._eventos)
        result.append(unicode(self.trailer))
        return '\n'.join(result)
