
import os
import codecs
from decimal import Decimal
from cnab240.bancos import itau

TESTS_DIRPATH = os.path.abspath(os.path.dirname(__file__))
ARQS_DIRPATH = os.path.join(TESTS_DIRPATH, 'arquivos')

HEADER_ARQUIVO_DICT = {
    'controle_banco': 1,
    'controle_lote': 2,
    'controle_registro': 0,
    'cnab1': u'',
    'cedente_inscricao_tipo': 2,
    'cedente_inscricao_numero': 12345678901234,
    'cedente_convenio': u'abcdefghijklmnopqrst',
    'cedente_agencia': 2891,
    'cedente_agencia_dv': u'6',
    'cedente_conta': 14262,
    'cedente_conta_dv': u'X',
    'cedente_agencia_conta_dv': u'7',
    'cedente_nome': u'Tracy Tecnologias LTDA ME',
    'nome_do_banco': u'Banco do Brasil',
    'cnab2': u'',
    'arquivo_codigo': 0,
    'arquivo_data_de_geracao': 20120713,
    'arquivo_hora_de_geracao': 220000,
    'arquivo_sequencia': 123456,
    'arquivo_layout': 85,
    'arquivo_densidade': 12345,
    'reservado_banco': u'',
    'reservado_cedente': u'',
    'cnab3': u'',
}

REGISTRO_T_DICT =  {
    u'controle_banco': 40,
    u'controle_lote': 6774,
    u'controle_registro': 3,
    u'servico_numero_registro': 1,
    u'servico_segmento': u'T',
    u'servico_cnab': u'',
    u'servico_codigo_movimento': 17,
    u'conta_agencia_codigo': 2260,
    u'conta_agencia_dv': u'8',
    u'conta_numero': 13000401,
    u'conta_dv': u'1',
    u'conta_agencia_conta_dv': u'0',
    u'nosso_numero': u'00000000000000000060',
    u'carteira': 1,
    u'numero_documento': u'',
    u'vencimento_titulo': 4082011,
    u'valor_titulo': Decimal('43.50'),
    u'banco_cobrador': 1,
    u'agencia_cobradora': 30,
    u'agencia_cobradora_dv': u'8',
    u'identificacao_titulo': u'',
    u'codigo_moeda': 0,
    u'sacado_inscricao_tipo': 2,
    u'sacado_inscricao_numero': 0,
    u'sacado_nome': u'',
    u'numero_contrato': 130004011,
    u'valor_tarifas': Decimal('2.64'),
    u'motivo_ocorrencia': u'0400000000',
    u'cnab': u'',
}

HEADER_ARQUIVO_STR = u'00100020         212345678901234abcdefghijklmnopqrst028916000000014262X7TRACY TECNOLOGIA LTDA ME      BANCO DO BRASIL                         02012071322000012345608512345                                                                     '

REGISTRO_T_STR = u'0336774300001T 1702260800001300040110000000000000000000601               04082011000000000004350001000308                         002000000000000000                                        01300040110000000000002640400000000                 '

# Dados Itau

SEG_P_ITAU_DICT = {
    u'aceite_titulo': u'A',
    u'agencia_cobradora': 0,
    u'agencia_cobradora_dv': 0,
    u'carteira_numero': 109,
    u'codigo_baixa': 0,
    u'codigo_protesto': 3,
    u'cedente_agencia': 4459,
    u'cedente_agencia_conta_dv': u'6',
    u'cedente_conta': 17600,
    u'controle_lote': 1,
    u'controle_registro': 3,
    u'data_emissao_titulo': 27062012,
    u'desconto1_codigo': 0,
    u'desconto1_data': 0,
    u'desconto1_percentual': Decimal('0.00'),
    u'especie_titulo': 8,
    u'identificacao_titulo': u'',
    u'juros_mora_codigo': 0,
    u'juros_mora_data': 0,
    u'juros_mora_taxa_dia': Decimal('2.00'),
    u'nosso_numero': 90000000,
    u'nosso_numero_dv': 2,
    u'numero_documento': u'9999999998',
    u'prazo_baixa': 0,
    u'prazo_protesto': 0,
    u'servico_codigo_movimento': 1,
    u'servico_numero_registro': 1,
    u'servico_segmento': u'P',
    u'valor_abatimento': Decimal('0.00'),
    u'valor_iof': Decimal('0.00'),
    u'valor_titulo': Decimal('100.00'),
    u'vencimento_titulo': 30062012
}

SEG_Q_ITAU_DICT = {
    u'controle_banco': 341,
    u'controle_lote': 1,
    u'controle_registro': 3,
    u'sacado_bairro': u'JD PALMARES',
    u'sacado_cep': 14092,
    u'sacado_cep_sufixo': 530,
    u'sacado_cidade': u'RIBEIRAO PRETO',
    u'sacado_endereco': u'RUA ARLINDO CATELLI 735 AP 12',
    u'sacado_inscricao_numero': 36644661874L,
    u'sacado_inscricao_tipo': 1,
    u'sacado_nome': u'DAVI OLIVEIRA CAMPOS',
    u'sacado_uf': u'SP',
    u'sacador_inscricao_numero': 15594050000111L,
    u'sacador_inscricao_tipo': 2,
    u'sacador_nome': u'TRACY TECNOLOGIA LTDA ME',
    u'servico_codigo_movimento': 1,
    u'servico_numero_registro': 2,
    u'servico_segmento': u'Q'
}

HEADER_COB_ITAU_DICT = {
    u'controle_banco': 341,
    u'controle_lote': 1,
    u'controle_registro': 1,
    u'controlecob_data_gravacao': 27062012,
    u'controlecob_numero': 90000001,
    u'data_credito': 0,
    u'cedente_agencia_conta_dv': u'6',
    u'cedente_agencia': 4459,
    u'cedente_agencia_dv': u'',
    u'cedente_conta': 17600,
    u'cedente_inscricao_numero': 15594050000111L,
    u'cedente_inscricao_tipo': 2,
    u'cedente_nome': u'TRACY TECNOLOGIA LTDA ME',
    u'servico_layout': 30,
    u'servico_operacao': u'R',
    u'servico_servico': 1
}

TRAILER_COB_ITAU_DICT = {
    u'cobrancasimples_quantidade_titulos': 2,
    u'cobrancasimples_valor_titulos': Decimal('300.00'),
    u'cobrancavinculada_quantidade_titulos': 0,
    u'cobrancavinculada_valor_titulos': Decimal('0.00'),
    u'controle_banco': 341,
    u'controle_lote': 1,
    u'controle_registro': 5,
    u'numero_aviso': u'',
}

SEG_P_ITAU_STR = u'3410001300001P 0104459 000000017600 6109900000002        000009999999998     3006201200000000001000000000008A27062012000000000000000000000200000000000000000000000000000000000000000000000000000000                         3000000000000000000 '

SEG_Q_ITAU_STR = u'3410001300002Q 011000036644661874DAVI OLIVEIRA CAMPOS                    RUA ARLINDO CATELLI 735 AP 12           JD PALMARES    14092530RIBEIRAO PRETO SP2015594050000111TRACY TECNOLOGIA LTDA ME                000                            '

