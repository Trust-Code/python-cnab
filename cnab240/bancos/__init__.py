
import os
import importlib

from cnab240.registro import Registros


cwd = os.path.abspath(os.path.dirname(__file__))
nome_bancos = (fname for fname in os.listdir(cwd)
               if os.path.isdir(os.path.join(cwd, fname)))

for nome_banco in nome_bancos:
    banco_module = importlib.import_module('.'.join((__package__, nome_banco)))
    module_path = os.path.abspath(os.path.dirname(banco_module.__file__))
    module_specs_path = os.path.join(module_path, 'specs')
    banco_module.registros = Registros(module_specs_path)
