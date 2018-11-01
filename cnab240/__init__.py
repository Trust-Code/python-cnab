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
    },
    '033': {
        '02': 'Entrada confirmada',
        '03': 'Entrada rejeitada',
        '04': 'Transferência de carteira/entrada',
        '05': 'Transferência de carteira/baixa',
        '06': 'Liquidação',
        '09': 'Baixa',
        '11': 'Títulos em carteira ( em ser)',
        '12': 'Confirmação recebimento instrução de abatimento',
        '13': 'Confirmação recebimento instrução de cancelamento abatimento',
        '14': 'Confirmação recebimento instrução alteração de vencimento',
        '17': 'Liquidação após baixa ou liquidação título não registrado',
        '19': 'Confirmação recebimento instrução de protesto',
        '20': 'Confirmação recebimento instrução de sustação/Não Protestar',
        '23': 'Remessa a cartorio ( aponte em cartorio)',
        '24': 'Retirada de cartorio e manutenção em carteira',
        '25': 'Protestado e baixado ( baixa por ter sido protestado)',
        '26': 'Instrução rejeitada',
        '27': 'Confirmação do pedido de alteração de outros dados',
        '28': 'Debito de tarifas/custas',
        '29': 'Ocorrências do Pagador',
        '30': 'Alteração de dados rejeitada',
        '32': 'Código de IOF inválido',
        '51': 'Título DDA reconhecido pelo Pagador',
        '52': 'Título DDA não reconhecido pelo Pagador',
        '53': 'Título DDA recusado pela CIP',
        '61': 'Confirmação de Alteração do Valor Nominal do Título',
        '91': 'Confirmação de Alteração do Valor Mínimo ou Percentual Mínimo',
        '92': 'Confirmação de Alteração do Valor Máximo ou Percentual Máximo',
        '93': 'Baixa Operacional',
        '94': 'Cancelamento de Baixa Operacional',
    }

}

PROCESSED_CODE = {
    '341': [2],
    '033': ['02'],
}

OK_CODE = {
    '341': [6, 8, 10],
    '033': ['06', '17'],
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
