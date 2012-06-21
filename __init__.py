
import os
import json

registro_specs = {}

cwd_path = os.path.abspath(os.path.dirname(__file__))
registros_dirpath = os.path.join(cwd_path, 'registros')

for registro_path in os.listdir(registros_dirpath):
    registro_file = open(os.path.join(registros_dirpath, registro_path))
    # TODO: Validar spec: nome (deve ser unico para cada registro), 
    #   posicao_inicio, posicao_fim, formato (alpha), decimais (0), 
    #   default (zeros se numerico ou brancos se alfa)
    spec = json.load(registro_file)
    registro_specs.update({os.path.splitext(registro_path)[0]: spec})
    registro_file.close()
