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
    },
    '756': {
        2: 'Entrada Confirmada',
        3: 'Entrada Rejeitada',
        4: 'Transferência de Carteira/Entrada',
        5: 'Transferência de Carteira/Baixa',
        6: 'Liquidação',
        7: 'Confirmação do Recebimento da Instrução de Desconto',
        8: 'Confirmação do Recebimento do Cancelamento do Desconto',
        9: 'Baixa',
        11: 'Títulos em Carteira (Em Ser)',
        12: 'Confirmação Recebimento Instrução de Abatimento',
        13: 'Confirmação Recebimento Instrução de Cancelamento Abatimento',
        14: 'Confirmação Recebimento Instrução Alteração de Vencimento',
        15: 'Franco de Pagamento',
        17: 'Liquidação Após Baixa ou Liquidação Título Não Registrado',
        19: 'Confirmação Recebimento Instrução de Protesto',
        20: 'Confirmação Recebimento Instrução de Sustação/Cancelamento de Protesto',  # noqa
        23: 'Remessa a Cartório (Aponte em Cartório)',
        24: 'Retirada de Cartório e Manutenção em Carteira',
        25: 'Protestado e Baixado (Baixa por Ter Sido Protestado)',
        26: 'Instrução Rejeitada',
        27: 'Confirmação do Pedido de Alteração de Outros Dados',
        28: 'Débito de Tarifas/Custas',
        29: 'Ocorrências do Pagador',
        30: 'Alteração de Dados Rejeitada',
        33: 'Confirmação da Alteração dos Dados do Rateio de Crédito',
        34: 'Confirmação do Cancelamento dos Dados do Rateio de Crédito',
        35: 'Confirmação do Desagendamento do Débito Automático',
        36: 'Confirmação de envio de e-mail/SMS',
        37: 'Envio de e-mail/SMS rejeitado',
        38: 'Confirmação de alteração do Prazo Limite de Recebimento',
        39: 'Confirmação de Dispensa de Prazo Limite de Recebimento',
        40: 'Confirmação da alteração do número do título dado pelo benefic.',
        41: 'Confirmação da alteração do número controle do Participante',
        42: 'Confirmação da alteração dos dados do Pagador',
        43: 'Confirmação da alteração dos dados do Sacador/Avalista',
        44: 'Título pago com cheque devolvido',
        45: 'Título pago com cheque compensado',
        46: 'Instrução para cancelar protesto confirmada',
        47: 'Instrução para protesto para fins falimentares confirmada',
        48: 'Confirmação de instrução de transferência de carteira/modalidade de cobrança',  # noqa
        49: 'Alteração de contrato de cobrança',
        50: 'Título pago com cheque pendente de liquidação',
        51: 'Título DDA reconhecido pelo pagador',
        52: 'Título DDA não reconhecido pelo pagador',
        53: 'Título DDA recusado pela CIP',
        54: 'Confirmação da Instrução de Baixa de Título Negativado sem Protesto',  # noqa
        55: 'Confirmação de Pedido de Dispensa de Multa',
        56: 'Confirmação do Pedido de Cobrança de Multa',
        57: 'Confirmação do Pedido de Alteração de Cobrança de Juros',
        58: 'Confirmação do Pedido de Alteração do Valor/Data de Desconto',
        59: 'Confirmação do Pedido de Alteração do Beneficiário do Título',
        60: 'Confirmação do Pedido de Dispensa de Juros de Mora',
    }
}

PROCESSED_CODE = {
    '341': [2],
    '033': ['02'],
    '756': [2],
}

BAIXA_CODE = {
    '341': [9],
    '033': ['09', '25', '93'],
    '756': [9, 25],
}

OK_CODE = {
    '341': [6, 8, 10],
    '033': ['06', '17'],
    '756': [6, 17],
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
        elif cnab_code in BAIXA_CODE[bank_code]:
            return '2222', message
        else:
            return cnab_code, message
    except KeyError:
        parse_keyerror(CNAB_CODE, bank_code, CNAB_CODE)
