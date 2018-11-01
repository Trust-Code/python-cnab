# -*- coding: utf-8 -*-

from cnab240 import bancos

BANK = {
    '237': bancos.bradesco,
    '756': bancos.sicoob,
    '341': bancos.itau,
    '001': bancos.banco_brasil,
    '0851': bancos.cecred,
    '033': bancos.santander,
    '748': bancos.sicredi,
}

CNAB_CODE = {
    '341': {
        2: 'ENTRADA CONFIRMADA',
        3: 'ENTRADA REJEITADA',
        4: 'ALTERAÇÃO DE DADOS – NOVA ENTRADA OU ALTERAÇÃO ACATADA',
        5: 'ALTERAÇÃO DE DADOS – BAIXA',
        6: 'LIQUIDAÇÃO NORMAL',
        8: 'LIQUIDAÇÃO EM CARTÓRIO',
        9: 'BAIXA SIMPLES',
        10: 'BAIXA POR TER SIDO LIQUIDADO',
        # TODO Implementar as outras mensagens
    }
}

PROCESSED_CODE = {
    '341': [2, 3],
}

OK_CODE = {
    '341': [6, 8, 10],
}


def parse_keyerror(dic, bank_name, code):
    message, value = 'Code', code
    if not dic.get(bank_name):
        message, value = 'Bank', bank_name
    raise KeyError("{} {} not found!".format(message, value))


def get_bank(bank_code):
    if bank_code in BANK:
        return BANK[bank_code]
    else:
        raise Exception('Código de banco inválido')


def parse_cnab_code(bank_code, cnab_code):
    try:
        message = CNAB_CODE[bank_code][cnab_code]
        if cnab_code in PROCESSED_CODE[bank_code]:
            return '1111', message
        elif cnab_code in OK_CODE[bank_code]:
            return '0000', message
        else:
            return cnab_code, message
    except KeyError:
        parse_keyerror(CNAB_CODE, bank_code, CNAB_CODE)
