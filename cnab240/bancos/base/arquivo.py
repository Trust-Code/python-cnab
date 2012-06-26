# -*- coding: utf-8 -*-

from datetime import datetime
from cnab240 import errors
from registro import Registro


class ArquivoCnab240(object):
    
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
        
        required_methods = ('HeaderArquivo', 'TrailerArquivo')
        if not all(hasattr(self, method) for method in required_methods):
            raise NotImplementedError
    
        self.header = self.HeaderArquivo()
        self.header.fromdict(kwargs)
        
        self.trailer = self.TrailerArquivo()
        self.trailer.fromdict(kwargs)        
        
        self._lotes = []

    @property
    def lotes(self):
        return lotes

    def __unicode__(self):
        if not self._lotes:
            raise errors.NenhumLoteError()
        
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

