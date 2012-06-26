
import os
import json
from glob import iglob

from registro import criar_classe_registro
from arquivo import ArquivoCnab240

class Banco(ArquivoCnab240): 

    ALIAS = None
    SPECS_DIRPATH = None

    def __init__(self):
        self.carregar_classes_registros()
        super(Banco, self).__init__()

    def carregar_classes_registros(self):
        if not self.SPECS_DIRPATH:
            raise NotImplementedError

        # TODO: Validar spec: nome (deve ser unico para cada registro),
        #   posicao_inicio, posicao_fim, formato (alpha), decimais (0),
        #   default (zeros se numerico ou brancos se alfa)
        registro_filepath_list = iglob(os.path.join(self.SPECS_DIRPATH,
                                                    '*.json'))

        for registro_filepath in registro_filepath_list:
            registro_file = open(registro_filepath)
            spec = json.load(registro_file)
            registro_file.close()

            setattr(self, spec.get('nome'), criar_classe_registro(spec))
