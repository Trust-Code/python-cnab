# -*- encoding: utf8 -*-

from datetime import datetime
from cnab240 import errors


class EventoBase(object):

    def __init__(self, banco):
        self._segmentos = []
        self.banco = banco 
        self._codigo_lote = None      
 
    @property
    def segmentos(self):    
        return self._segmentos
    
    def __getattribute__(self, name):
        for segmento in object.__getattribute__(self, '_segmentos'):
            if hasattr(segmento, name):
                return getattr(segmento, name)
        return object.__getattribute__(self, name)
    
    def __unicode__(self):
        return u'\n'.join(unicode(seg) for seg in self._segmentos)

    def __len__(self):
        return len(self._segmentos)

    @property
    def codigo_lote(self):
        return self._codigo_lote

    @codigo_lote.setter
    def codigo_lote(self, valor):
        self._codigo_lote = valor
        for segmento in self._segmentos:
            segmento.controle_lote = valor  

class LoteBase(object):

    def __init__(self, banco, header, trailer):
        self.banco = banco 
        self.header = header
        self.trailer = trailer
        self._codigo = None
        self.trailer.quantidade_registros = 2
        self._eventos = []

    @property
    def codigo(self):
        return self._codigo   

    @codigo.setter
    def codigo(self, valor):
        self._codigo = valor
        self.header.controle_lote = valor
        self.trailer.controle_lote = valor

        for evento in self._eventos:
            evento.codigo_lote = valor

    @property
    def eventos(self):
        return self._eventos   
 
    def adicionar_evento(self, evento):
        if not isinstance(evento, EventoBase):
            raise TypeError
        
        self._eventos.append(evento)
        self.trailer.quantidade_registros += len(evento)

    def __unicode__(self):
        if not self._eventos:
            raise errors.NenhumEventoError()
    
        result = [] 
        result.append(unicode(self.header))
        result.extend(unicode(evento) for evento in self._eventos)
        result.append(unicode(self.trailer))
        return '\n'.join(result)

    def __len__(self):
        return self.trailer.quantidade_registros


class Arquivo(object):

    def __init__(self, banco, **kwargs):
        """Arquivo Cnab240.""" 

        self._lotes = []
        self.banco = banco
            
        self.header = self.banco.registros.HeaderArquivo(**kwargs) 
        self.trailer = self.banco.registros.TrailerArquivo(**kwargs)
        self.trailer.totais_quantidade_lotes = 0        
        self.trailer.totais_quantidade_registros = 2
        
    @property
    def lotes(self):
        return lotes
        
    def adicionar_lote(self, lote):
        if not isinstance(lote, LoteBase):
            raise TypeError('Objeto deve ser instancia de "LoteBase"')

        self._lotes.append(lote)
        
        lote.codigo = len(self._lotes)

        # Incrementar numero de lotes no trailer do arquivo
        self.trailer.totais_quantidade_lotes += 1

        # Incrementar numero de registros no trailer do arquivo
        self.trailer.totais_quantidade_registros += len(lote)

    def escrever(self, file_):
        file_.write(unicode(self.encode('ascii')))

    def __unicode__(self):
        if not self._lotes:
            raise errors.ArquivoVazioError()
        
        result = []
        result.append(unicode(self.header))
        result.extend(unicode(lote) for lote in self._lotes)
        result.append(unicode(self.trailer))
        return u'\n'.join(result)

