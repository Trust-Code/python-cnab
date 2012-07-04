# -*- encoding: utf8 -*-

import importlib
from datetime import datetime
from cnab240 import errors


class EventoBase(object):

    def __init__(self, banco, codigo_evento):
        self._segmentos = []
        self.banco = banco 
        self.codigo_evento = codigo_evento
        self._codigo_lote = None
        
    def adicionar_segmento(self, segmento):
        self._segmentos.append(segmento) 
        for segmento in self._segmentos:
            segmento.servico_codigo_movimento = self.codigo_evento
 
    @property
    def segmentos(self):    
        return self._segmentos

    def clean_kwargs(self, data_dict):
        ignore_fields = lambda key: any((
            key.startswith('vazio'), 
            key.startswith('servico_'),
            key.startswith('controle_'),
        ))
        return dict((key, value) for key, value in data_dict.items()
                         if not ignore_fields(key))
    
    def __getattribute__(self, name):
        for segmento in object.__getattribute__(self, '_segmentos'):
            if hasattr(segmento, name):
                return getattr(segmento, name)
        return object.__getattribute__(self, name)
    
    def __unicode__(self):
        return u'\r\n'.join(unicode(seg) for seg in self._segmentos)

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
    
    def atualizar_codigo_registros(self, last_id):
        current_id = last_id 
        for segmento in self._segmentos:
            current_id += 1
            segmento.servico_numero_registro = current_id
        return current_id

class Lote(object):

    def __init__(self, banco, header=None, trailer=None):
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
        self.atualizar_codigo_eventos()

    def atualizar_codigo_eventos(self):
        for evento in self._eventos:
            evento.codigo_lote = self._codigo

    def atualizar_codigo_registros(self):
        last_id = 0
        for evento in self._eventos:       
             last_id = evento.atualizar_codigo_registros(last_id) 
 
    @property
    def eventos(self):
        return self._eventos   
 
    def adicionar_evento(self, evento):
        if not isinstance(evento, EventoBase):
            raise TypeError
        
        self._eventos.append(evento)
        self.trailer.quantidade_registros += len(evento)
        self.atualizar_codigo_registros()        
        
        if self._codigo:
            self.atualizar_codigo_eventos()

    def __unicode__(self):
        if not self._eventos:
            raise errors.NenhumEventoError()
    
        result = [] 
        result.append(unicode(self.header))
        result.extend(unicode(evento) for evento in self._eventos)
        result.append(unicode(self.trailer))
        return '\r\n'.join(result)

    def __len__(self):
        return self.trailer.quantidade_registros


class Arquivo(object):

    def __init__(self, banco, **kwargs):
        """Arquivo Cnab240.""" 

        self._lotes = []
        self.banco = banco
        
        arg_dict = dict((key, value) for key, value in kwargs.items()
                         if not key.startswith('vazio'))
         
        self.header = self.banco.registros.HeaderArquivo(**args_dict) 
        self.trailer = self.banco.registros.TrailerArquivo(**args_dict)
        self.trailer.totais_quantidade_lotes = 0        
        self.trailer.totais_quantidade_registros = 2
        
    @property
    def lotes(self):
        return lotes
        
    def adicionar_lote(self, lote):
        if not isinstance(lote, Lote):
            raise TypeError('Objeto deve ser instancia de "Lote"')

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

