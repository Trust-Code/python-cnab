
import cnab240

from decimal import Decimal


class Registro(object):

    def __init__(self, nome):
        self.spec = cnab240.registro_specs.get(nome)
        if not self.spec:
            # TODO:
            raise Exception

    def le_campo(self, campo_code, campo_spec, registro_str):
        inicio = campo_spec.get('posicao_inicio') - 1
        fim = campo_spec.get('posicao_fim')
        formato = campo_spec.get('formato', 'alfa') 
        decimais = campo_spec.get('decimais', 0) 
        
        valor = registro_str[inicio:fim].strip()
        if formato == 'num'
            if not decimais:
                try:
                    valor = int(valor)
                except ValueError:
                    # TODO:
                    raise Exception

            else:
                try:
                    valor = Decimal(valor[:decimais] + '.' + valor[decimais:])
                except InvalidOperation:
                    # TODO:
                    raise Exception

        return valor 
    
    def loads(self, registro_str):
        """
        Exemplo de registro_str: 
00100000         212345678901234abcdefghijklmnopqrst028916000000014262X7TRACY TECNOLOGIA LTDA ME      BANCO DO BRASIL                         020120713220000123456085 
        """       
 
        for campo_code, campo_spec in self.spec.get('campos', {}).items():
            value = self.le_campo(campo_code, campo_spec, registro_str)
            setattr(self, campo_spec.get('nome'), value)

    
