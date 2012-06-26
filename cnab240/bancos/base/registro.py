
import os
import json

from glob import iglob
from decimal import Decimal, InvalidOperation
from collections import OrderedDict
from cnab240 import errors
from cnab240.campo import Campo
from cnab240.base import TipoCnab240


class Registro(object):

    def fromdict(self, dict_):
        pass

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


def criar_classe_registro(spec):

    campos = OrderedDict()
    attrs = {'_campos': campos}

    campo_specs = spec.get('campos', {})
    for key in sorted(campo_specs.iterkeys()):
        campo = Campo(campo_specs[key])
        campos.update({campo.nome: campo})
        attrs.update({campo.nome: campo})

    return type(spec.get('nome').encode('utf8'), (Registro, ), attrs)

