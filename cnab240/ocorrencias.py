# -*- coding: utf-8 -*-

CODIGO_MOTIVOS_OCORRENCIA = {
    '02': {
        'codigo_ocorrencia': '02',
        'texto': 'Entrada confirmada',
        '00': 'Ocorrência aceita',
        '01': 'Código do Banco inválido',
        '04': 'Código do movimento não permitido para a carteira (NOVO)',
        '15': 'Características da cobrança incompatíveis (NOVO)',
        '17': 'Data de vencimento anterior a data de emissão',
        '21': 'Espécie do Título inválido',
        '24': 'Data da emissão inválida',
        '27': 'Valor/taxa de juros mora inválido (NOVO)',
        '38': 'Prazo para protesto/ Negativação inválido (ALTERADO)',
        '39': 'Pedido para protesto/ Negativação não permitido'
              ' para o título (ALTERADO)',
        '43': 'Prazo para baixa e devolução inválido',
        '45': 'Nome do Pagador inválido',
        '46': 'Tipo/num. de inscrição do Pagador inválidos',
        '47': 'Endereço do Pagador não informado',
        '48': 'CEP Inválido',
        '50': 'CEP referente a Banco correspondente',
        '53': 'No de inscrição do Pagador/avalista inválidos (CPF/CNPJ)',
        '54': 'Pagadorr/avalista não informado',
        '67': 'Débito automático agendado',
        '68': 'Débito não agendado - erro nos dados de remessa',
        '69': 'Débito não agendado - Pagador não consta '
              'no cadastro de autorizante',
        '70': 'Débito não agendado - Beneficiário não autorizado pelo Pagador',
        '71': 'Débito não agendado - Beneficiário não participa '
              'da modalidade de déb.automático',
        '72': 'Débito não agendado - Código de moeda diferente de R$',
        '73': 'Débito não agendado - Data de vencimento inválida/vencida',
        '75': 'Débito não agendado - Tipo do número de inscrição '
              'do pagador debitado inválido',
        '76': 'Pagador Eletrônico DDA (NOVO)- Esse motivo somente '
              'será disponibilizado no arquivo retorno para as '
              'empresas cadastradas nessa condição.',
        '86': 'Seu número do documento inválido',
        '89': 'Email Pagador não enviado – título com débito automático (NOVO)',
        '90': 'Email pagador não enviado – título de cobrança '
              'sem registro (NOVO)',
    },
    '03': {
        'codigo_ocorrencia': '03',
        'texto': 'entrada rejeitada',
        '00': 'N/A',
        '02': 'Código do registro detalhe inválido',
        '03': 'Código da ocorrência inválida',
        '04': 'Código de ocorrência não permitida para a carteira',
        '05': 'Código de ocorrência não numérico',
        '07': 'Agência/conta/Digito - |Inválido',
        '08': 'Nosso número inválido',
        '09': 'Nosso número duplicado',
        '10': 'Carteira inválida',
        '13': 'Identificação da emissão do bloqueto inválida (NOVO)',
        '16': 'Data de vencimento inválida',
        '18': 'Vencimento fora do prazo de operação',
        '20': 'Valor do Título inválido',
        '21': 'Espécie do Título inválida',
        '22': 'Espécie não permitida para a carteira',
        '24': 'Data de emissão inválida',
        '28': 'Código do desconto inválido (NOVO)',
        '38': 'Prazo para protesto/ Negativação inválido (ALTERADO)',
        '44': 'Agência Beneficiário não prevista',
        '45': 'Nome do pagador não informado (NOVO)',
        '46': 'Tipo/número de inscrição do pagador inválidos (NOVO)',
        '47': 'Endereço do pagador não informado (NOVO)',
        '48': 'CEP Inválido (NOVO)',
        '50': 'CEP irregular - Banco Correspondente',
        '63': 'Entrada para Título já cadastrado',
        '65': 'Limite excedido (NOVO)',
        '66': 'Número autorização inexistente (NOVO)',
        '68': 'Débito não agendado - erro nos dados de remessa',
        '69': 'Débito não agendado - Pagador não consta '
              'no cadastro de autorizante',
        '70': 'Débito não agendado - Beneficiário não autorizado pelo Pagador',
        '71': 'Débito não agendado - Beneficiário não participa '
              'do débito Automático',
        '72': 'Débito não agendado - Código de moeda diferente de R$',
        '73': 'Débito não agendado - Data de vencimento inválida',
        '74': 'Débito não agendado - Conforme seu pedido, '
              'Título não registrado',
        '75': 'Débito não agendado – Tipo de número de '
              'inscrição do debitado inválido',
    },

    '06': {
        'codigo_ocorrencia': '06',
        'texto': 'Liquidação normal',
        '00': 'Título pago com dinheiro',
        '15': 'Título pago com cheque',
        '42': 'Rateio não efetuado, cód. Calculo 2 (VLR. Registro) e v (NOVO)'
    },

    '10': {
        'codigo_ocorrencia': '10',
        'texto': 'Baixado conforme instruções da Agência',
        '00': 'Baixado Conforme Instruções da Agência',
        '14': 'Título Protestado',
        '15': 'Título excluído',
        '16': 'Título Baixado pelo Banco por decurso Prazo',
        '17': 'Titulo Baixado Transferido Carteira',
        '20': 'Titulo Baixado e Transferido para Desconto',
    },

    '12': {
        'codigo_ocorrencia': '12',
        'texto': 'Abatimento Concedido',
        '00': 'N/A',
    },

    '14': {
        'codigo_ocorrencia': '14',
        'texto': 'Vencimento Alterado',
        '00': 'N/A',
    },

    '15': {
        'codigo_ocorrencia': '15',
        'texto': 'Liquidação em cartório',
        '00': 'Título pago com dinheiro',
        '15':'Título pago com cheque',
    },

    '16': {
        'codigo_ocorrencia': '16',
        'texto': 'Título pago em cheque',
        '00': 'Vinculado',
    },

    '17': {
        'codigo_ocorrencia': '17',
        'texto': 'Liquidação após baixa ou Título não registrado',
        '00': 'Título pago com dinheiro',
        '15': 'Título pago com cheque'
    },

    '19': {
        'codigo_ocorrencia': '19',
        'texto': 'Confirmação Receb. Inst. de Protesto',
        '00': 'N/A',
    },

    '23': {
        'codigo_ocorrencia': '23',
        'texto': 'Entrada do Título em Cartório',
        '00': 'N/A',
    },

    '24': {
        'codigo_ocorrencia': '24',
        'texto': 'Entrada rejeitada por CEP Irregular',
        '00': '',
        '48': 'CEP inválido',
    },

    '28': {
        'codigo_ocorrencia': '28',
        'texto': 'Débito de tarifas/custas',
        '00': 'N/A',
        '02': 'Tarifa de permanência título cadastrado (NOVO)',
        '03': 'Tarifa de sustação/Excl Negativação (ALTERADO)',
        '04': 'Tarifa de protesto/Incl Negativação (ALTERADO)',
        '05': 'Tarifa de outras instruções (NOVO)',
        '06': 'Tarifa de outras ocorrências (NOVO)',
        '08': 'Custas de protesto',
        '12': 'Tarifa de registro (NOVO)',
        '13': 'Tarifa título pago no Bradesco (NOVO)',
        '14': 'Tarifa título pago compensação (NOVO)',
        '15': 'Tarifa título baixado não pago (NOVO)',
        '16': 'Tarifa alteração de vencimento (NOVO)',
        '17': 'Tarifa concessão abatimento (NOVO)',
        '18': 'Tarifa cancelamento de abatimento (NOVO)',
        '19': 'Tarifa concessão desconto (NOVO)',
        '20': 'Tarifa cancelamento desconto (NOVO)',
        '21': 'Tarifa título pago cics (NOVO)',
        '22': 'Tarifa título pago Internet (NOVO)',
        '23': 'Tarifa título pago term. gerencial serviços (NOVO)',
        '24': 'Tarifa título pago Pág-Contas (NOVO)',
        '25': 'Tarifa título pago Fone Fácil (NOVO)',
        '26': 'Tarifa título Déb. Postagem (NOVO)',
        '27': 'Tarifa impressão de títulos pendentes (NOVO)',
        '28': 'Tarifa título pago BDN (NOVO)',
        '29': 'Tarifa título pago Term. Multi Função (NOVO)',
        '30': 'Impressão de títulos baixados (NOVO)',
        '31': 'Impressão de títulos pagos (NOVO)',
        '32': 'Tarifa título pago Pagfor (NOVO)',
        '33': 'Tarifa reg/pgto – guichê caixa (NOVO)',
        '34': 'Tarifa título pago retaguarda (NOVO)',
        '35': 'Tarifa título pago Subcentro (NOVO)',
        '36': 'Tarifa título pago Cartão de Crédito (NOVO)',
        '37': 'Tarifa título pago Comp Eletrônica (NOVO)',
        '38': 'Tarifa título Baix. Pg. Cartório (NOVO)',
        '39': 'Tarifa título baixado acerto BCO (NOVO)',
        '40': 'Baixa registro em duplicidade (NOVO)',
        '41': 'Tarifa título baixado decurso prazo (NOVO)',
        '42': 'Tarifa título baixado Judicialmente (NOVO)',
        '43': 'Tarifa título baixado via remessa (NOVO)',
        '44': 'Tarifa título baixado rastreamento (NOVO)',
        '45': 'Tarifa título baixado conf. Pedido (NOVO)',
        '46': 'Tarifa título baixado protestado (NOVO)',
        '47': 'Tarifa título baixado p/ devolução (NOVO)',
        '48': 'Tarifa título baixado franco pagto (NOVO)',
        '49': 'Tarifa título baixado SUST/RET/CARTÓRIO (NOVO)',
        '50': 'Tarifa título baixado SUS/SEM/REM/CARTÓRIO (NOVO)',
        '51': 'Tarifa título transferido desconto (NOVO)',
        '52': 'Cobrado baixa manual (NOVO)',
        '53': 'Baixa por acerto cliente (NOVO)',
        '54': 'Tarifa baixa por contabilidade (NOVO)',
        '55': 'Tr. tentativa cons deb aut',
        '56': 'Tr. credito online',
        '57': 'Tarifa reg/pagto Bradesco Expresso',
        '58': 'Tarifa emissão Papeleta (NOVO)',
        '59': 'Tarifa fornec papeleta semi preenchida (NOVO)',
        '60': 'Acondicionador de papeletas (RPB)S (NOVO)',
        '61': 'Acond. De papelatas (RPB)s PERSONAL (NOVO)',
        '62': 'Papeleta formulário branco (NOVO)',
        '63': 'Formulário A4 serrilhado (NOVO)',
        '64': 'Fornecimento de softwares transmiss (NOVO)',
        '65': 'Fornecimento de softwares consulta (NOVO)',
        '66': 'Fornecimento Micro Completo (NOVO)',
        '67': 'Fornecimento MODEN (NOVO)',
        '68': 'Fornecimento de máquina FAX (NOVO)',
        '69': 'Fornecimento de máquinas óticas (NOVO)',
        '70': 'Fornecimento de Impressoras (NOVO)',
        '71': 'Reativação de título (NOVO)',
        '72': 'Alteração de produto negociado (NOVO)',
        '73': 'Tarifa emissão de contra recibo (NOVO)',
        '74': 'Tarifa emissão 2a via papeleta (NOVO)',
        '75': 'Tarifa regravação arquivo retorno (NOVO)',
        '76': 'Arq. Títulos a vencer mensal (NOVO)',
        '77': 'Listagem auxiliar de crédito (NOVO)',
        '78': 'Tarifa cadastro cartela instrução permanente (NOVO)',
        '79': 'Canalização de Crédito (NOVO)',
        '80': 'Cadastro de Mensagem Fixa (NOVO)',
        '81': 'Tarifa reapresentação automática título (NOVO)',
        '82': 'Tarifa registro título déb. Automático (NOVO)',
        '83': 'Tarifa Rateio de Crédito (NOVO)',
        '84': 'Emissão papeleta sem valor (NOVO)',
        '85': 'Sem uso (NOVO)',
        '86': 'Cadastro de reembolso de diferença (NOVO)',
        '87': 'Relatório fluxo de pagto (NOVO)',
        '88': 'Emissão Extrato mov. Carteira (NOVO)',
        '89': 'Mensagem campo local de pagto (NOVO)',
        '90': 'Cadastro Concessionária serv. Publ. (NOVO)',
        '91': 'Classif. Extrato Conta Corrente (NOVO)',
        '92': 'Contabilidade especial (NOVO)',
        '93': 'Realimentação pagto (NOVO)',
        '94': 'Repasse de Créditos (NOVO)',
        '96': 'Tarifa reg. Pagto outras mídias (NOVO)',
        '97': 'Tarifa Reg/Pagto – Net Empresa (NOVO)',
        '98': 'Tarifa título pago vencido (NOVO)',
        '99': 'TR Tít. Baixado por decurso prazo (NOVO)',
        # '100': 'Arquivo Retorno Antecipado (NOVO)',
        # '101': 'Arq retorno Hora/Hora (NOVO)',
        # '102': 'TR. Agendamento Déb Aut (NOVO)',
        # '105': 'TR. Agendamento rat. Crédito (NOVO)',
        # '106': 'TR Emissão aviso rateio (NOVO)',
        # '107': 'Extrato de protesto (NOVO)',
    },

    '32': {
        'codigo_ocorrencia': '32',
        'texto': 'Instrução Rejeitada',
        '00': 'N/A',
        '01': 'Código do Banco inválido',
        '02': 'Código do registro detalhe inválido',
        '04': 'Código de ocorrência não permitido para a carteira',
        '05': 'Código de ocorrência não numérico',
        '07': 'Agência/Conta/dígito inválidos',
        '08': 'Nosso número inválido',
        '10': 'Carteira inválida',
        '15': 'Características da cobrança incompatíveis',
        '16': 'Data de vencimento inválida',
        '17': 'Data de vencimento anterior a data de emissão',
        '18': 'Vencimento fora do prazo de operação',
        '20': 'Valor do título inválido',
        '21': 'Espécie do Título inválida',
        '22': 'Espécie não permitida para a carteira',
        '24': 'Data de emissão inválida',
        '28': 'Código de desconto via Telebradesco inválido',
        '29': 'Valor do desconto maior/igual ao valor do Título',
        '30': 'Desconto a conceder não confere',
        '31': 'Concessão de desconto - Já existe desconto anterior',
        '33': 'Valor do abatimento inválido',
        '34': 'Valor do abatimento maior/igual ao valor do Título',
        '36': 'Concessão abatimento - Já existe abatimento anterior',
        '38': 'Prazo para protesto/ Negativação inválido (ALTERADO)',
        '39': 'Pedido para protesto/ Negativação não '
              'permitido para o título (ALTERADO)',
        '40': 'Título com ordem/pedido de '
              'protesto/Negativação emitido (ALTERADO)',
        '41': 'Pedido de sustação/excl p/ '
              'Título sem instrução de protesto/Negativação (ALTERADO)',
        '42': 'Código para baixa/devolução inválido',
        '45': 'Nome do Pagador não informado',
        '46': 'Tipo/número de inscrição do Pagador inválidos',
        '47': 'Endereço do Pagador não informado',
        '48': 'CEP Inválido',
        '50': 'CEP referente a um Banco correspondente',
        '53': 'Tipo de inscrição do pagador avalista inválidos',
        '60': 'Movimento para Título não cadastrado',
        '85': 'Título com pagamento vinculado',
        '86': 'Seu número inválido',
        '94': 'Título Penhorado – Instrução Não Liberada pela Agência (NOVO)',
        '97': ' Instrução não permitida título negativado (NOVO)',
        '98': ' Inclusão Bloqueada face a determinação Judicial (NOVO)',
        '99': ' Telefone beneficiário não informado / inconsistente (NOVO)',
    },

    '33': {
        'codigo_ocorrencia': '33',
        'texto': 'Confirmação Pedido Alteração Outros Dados',
        '00': 'N/A',

    },
}


def retorna_ocorrencia(identificacao_ocorrencia):
    identificacao_ocorrencia = str(identificacao_ocorrencia)

    if len(identificacao_ocorrencia) < 2:
        identificacao_ocorrencia = '0' + identificacao_ocorrencia

    return CODIGO_MOTIVOS_OCORRENCIA[identificacao_ocorrencia]['texto']


def retorna_motivios_ocorrencia(identificacao_ocorrencia, id_motivos):
    motivos = ['', '', '', '', '']

    identificacao_ocorrencia = str(identificacao_ocorrencia)

    if len(identificacao_ocorrencia) < 2:
        identificacao_ocorrencia = '0' + identificacao_ocorrencia

    if CODIGO_MOTIVOS_OCORRENCIA[identificacao_ocorrencia][id_motivos[:2]]\
            not in motivos:
        motivos[0] = CODIGO_MOTIVOS_OCORRENCIA[identificacao_ocorrencia][
            id_motivos[:2]]

    if CODIGO_MOTIVOS_OCORRENCIA[identificacao_ocorrencia][id_motivos[2:4]]\
            not in motivos:
        motivos[1] = CODIGO_MOTIVOS_OCORRENCIA[identificacao_ocorrencia][
            id_motivos[2:4]]

    if CODIGO_MOTIVOS_OCORRENCIA[identificacao_ocorrencia][id_motivos[4:6]]\
            not in motivos:
        motivos[2] = CODIGO_MOTIVOS_OCORRENCIA[identificacao_ocorrencia][
            id_motivos[4:6]]

    if CODIGO_MOTIVOS_OCORRENCIA[identificacao_ocorrencia][id_motivos[6:8]]\
            not in motivos:
        motivos[3] = CODIGO_MOTIVOS_OCORRENCIA[identificacao_ocorrencia][
            id_motivos[6:8]]

    if CODIGO_MOTIVOS_OCORRENCIA[
           identificacao_ocorrencia][id_motivos[8:10]] not in motivos:
        motivos[4] = CODIGO_MOTIVOS_OCORRENCIA[identificacao_ocorrencia][
            id_motivos[8:10]]

    return motivos
