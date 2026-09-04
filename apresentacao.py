SIMBOLOS_OPERACOES = {
    "1": "+",
    "2": "-",
    "3": "x",
    "4": "÷",
    "5": "%"
}

#=====        Símbolo da Operação        =====
def simbolo_operacao(operacao):
    return SIMBOLOS_OPERACOES[operacao]

#=====        Formatar Resultado        =====
def formatar_resultado(numero1, numero2, operacao, resultado):
    if operacao == "5":
        return f"{numero1}{simbolo_operacao(operacao)} de {numero2} = {resultado}"
    else:
        return f"{numero1} {simbolo_operacao(operacao)} {numero2} = {resultado}"

#=====        Exibir Resultado        =====
def mostrar_resultado(numero1, numero2, operacao, resultado):
    print(formatar_resultado(numero1, numero2, operacao, resultado))