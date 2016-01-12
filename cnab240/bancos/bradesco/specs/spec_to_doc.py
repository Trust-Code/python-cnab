#!/usr/bin/env python

import sys
import json
from collections import OrderedDict

fname = sys.argv[1]
f = file(fname)
spec = json.load(f, object_pairs_hook=OrderedDict)
f.close()

campos = spec.get('campos')
for campo in campos.values():
    campo_nome = campo.get('nome')
    campo_formato = campo.get('formato')
    campo_decimais = campo.get('decimais')
    
    if campo_decimais:
        tipo = 'Decimal ({0} digitos)'.format(campo_decimais)
    elif campo_formato == 'alfa':   
        tipo = 'str'
    else:
        tipo = 'int'
    
    print (' '* 8) + ':param {0}:'.format(campo_nome)
    print (' '* 8) + ':type {0}: {1}'.format(campo_nome, tipo)
    print 
 
