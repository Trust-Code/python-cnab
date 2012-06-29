# -*- encoding: utf8 -*-

from datetime import datetime
from cnab240 import errors


class ArquivoBase(object):

    banco = None

    def __init__(self, **kwargs):
        """Arquivo Cnab240. 
      
        :param empresa_inscricao_tipo: Tipo de Inscrição da Empresa
        :type empresa_inscricao_tipo: int

        :param empresa_inscricao_numero: Número de Inscrição da Empresa
        :type empresa_inscricao_numero: int

        :param empresa_convenio: Código do Convênio no Banco
        :type :empresa_convenio: str

        :param empresa_conta_agencia_codigo: Agência Mantenedora da Conta
        :type empresa_conta_agencia_codigo: int

        :param empresa_conta_agencia_dv: Dígito Verificador da Agência
        :type empresa_conta_agencia_dv: str 

        :param empresa_conta_numero: Número da Conta Corrente
        :type empresa_conta_numero: int

        :param empresa_conta_dv: Dígito Verificador da Conta
        :type empresa_conta_dv: str 

        :param empresa_agencia_conta_dv: Dígito Verificador da Ag/Conta
        :type empresa_agencia_conta_dv: str

        :param empresa_nome: Nome da Empresa
        :type empresa_nome: str

        :param nome_do_banco: Nome do Banco
        :type nome_do_banco: str

        :param arquivo_codigo: Código Remessa / Retorno
        :type arquivo_codigo: int

        :param arquivo_data_de_geracao: Data de Geração do Arquivo
        :type arquivo_data_de_geracao: int

        :param arquivo_hora_de_geracao: Hora de Geração do Arquivo
        :type arquivo_hora_de_geracao: int

        :param arquivo_sequencia: Número Seqüencial do Arquivo
        :type arquivo_sequencia: int

        :param arquivo_layout: No da Versão do Layout do Arquivo
        :type arquivo_layout: int

        :param arquivo_densidade: Densidade de Gravação do Arquivo
        :type arquivo_densidade: int

        :param reservado_banco: Para Uso Reservado do Banco
        :type reservado_banco: str

        :param reservado_empresa: Para Uso Reservado da Empresa
        :type reservado_empresa: str

        """

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
    def __init__(self, **kwargs):
        self._segmentos = [] 
       
    @property
    def segmentos(self):    
        return self._segmentos
    
    def __getattribute__(self, name):
        for segmento in object.__getattribute__(self,'_segmentos'):
            if hasattr(segmento, name):
                return getattr(segmento, name)
        return object.__getattribute__(self, name)
    
    def __unicode__(self):
        return u'\n'.join(unicode(seg) for seg in self._segmentos)


class LoteBase(object):

    eventos_validos = None
 
    def __init__(self, banco):
        if self.eventos_validos is None:
            raise NotImplementedError
        
        self.banco = banco
    
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
