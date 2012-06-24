
import os
import json
import errors

from glob import iglob
from decimal import Decimal, InvalidOperation
from collections import OrderedDict
from cnab240.campo import Campo
from cnab240.base import TipoCnab240

REGISTRO_SPECS = {}


class Registro(object):

    def __new__(cls, nome, versao):

        spec = REGISTRO_SPECS.get(versao, {}).get(nome, {})
        campos = OrderedDict()
        attrs = {'_campos': campos}

        campo_specs = spec.get('campos', {})
        for key in sorted(campo_specs.iterkeys()):
            campo = Campo(campo_specs[key])
            campos.update({campo.nome: campo})
            attrs.update({campo.nome: campo})

        new_cls = type('Registro', (RegistroBase, ), attrs)
        return new_cls(versao=versao)


class RegistroBase(TipoCnab240):

    def carregar(self, registro_str):

        for campo in self._campos.values():

            valor = registro_str[campo.inicio:campo.fim].strip()
            if campo.formato == 'num' and campo.decimais:
                exponente = campo.decimais * -1
                dec = valor[:exponente] + '.' + valor[exponente:]
                try:
                    campo.valor = Decimal(dec)
                except InvalidOperation:
                    raise # raise custom?

            elif campo.formato == 'num':
                try:
                    campo.valor = int(valor)
                except ValueError:
                    raise errors.TipoError(campo, valor)
            else:
                campo.valor = valor

    def __unicode__(self):
        return ''.join([unicode(campo) for campo in self._campos.values()])


def load_register_specs():
    # TODO: Validar spec: nome (deve ser unico para cada registro),
    #   posicao_inicio, posicao_fim, formato (alpha), decimais (0),
    #   default (zeros se numerico ou brancos se alfa)
    cwd_path = os.path.abspath(os.path.dirname(__file__))
    specs_dirpath = os.path.join(cwd_path, 'registros')
    for version in os.listdir(specs_dirpath):
        specs = {}
        REGISTRO_SPECS.update({version: specs})
        registro_filepath_list = iglob(os.path.join(specs_dirpath,
                                                    version, '*.json'))
        for registro_filepath in registro_filepath_list:
            registro_file = open(registro_filepath)
            spec = json.load(registro_file)
            specs.update({spec.get('nome'): spec})
            registro_file.close()

load_register_specs()
