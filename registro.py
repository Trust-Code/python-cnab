
import os                                                                        
import json                                                                      
                                                                                 
from decimal import Decimal, InvalidOperation
from collections import OrderedDict
from campo import Campo


REGISTRO_SPECS = {}


class Registro(object):

    def __new__(cls, nome):
        
        spec = REGISTRO_SPECS.get(nome, {})
        campos = OrderedDict()
        attrs = {'_campos': campos}

        campo_specs = spec.get('campos', {})
        for key in sorted(campo_specs.iterkeys()):
            campo = Campo(campo_specs[key])
            campos.update({campo.nome: campo})
            attrs.update({campo.nome: campo})

        new_cls = type('Registro', (RegistroBase, ), attrs)
        return new_cls() 


class RegistroBase(object):

    def carregar(self, registro_str):
 
        for campo in self._campos.values():
            
            valor = registro_str[campo.inicio:campo.fim].strip()
            if campo.formato == 'num' and campo.decimais:
                dec = valor[:campo.decimais] + '.' + valor[campo.decimais:]
                try:
                    campo.valor = Decimal(dec)
                except InvalidOperation:
                    raise # raise custom? 

            elif campo.formato == 'num':
                try:
                    campo.valor = int(valor)
                except ValueError:
                    raise # raise custom? 
            else:
                campo.valor = valor

    def escreve(self):
        return ''.join([unicode(campo) for campo in self._campos.values()])  


cwd_path = os.path.abspath(os.path.dirname(__file__))                            
registros_dirpath = os.path.join(cwd_path, 'registros')                          
for registro_path in os.listdir(registros_dirpath):                              
    registro_file = open(os.path.join(registros_dirpath, registro_path))         
    # TODO: Validar spec: nome (deve ser unico para cada registro), 
    #   posicao_inicio, posicao_fim, formato (alpha), decimais (0), 
    #   default (zeros se numerico ou brancos se alfa)                           
    spec = json.load(registro_file)                                              
    REGISTRO_SPECS.update({os.path.splitext(registro_path)[0]: spec})            
    registro_file.close()      

