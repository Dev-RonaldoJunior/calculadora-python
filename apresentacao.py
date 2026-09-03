SIMBOLOS_OPERACOES = {
    "1": "+",
    "2": "-",
    "3": "x",
    "4": "÷"
}

#=====        Símbolo da Operação        =====
def simbolo_operacao(operacao):
    return SIMBOLOS_OPERACOES[operacao]

#=====        Exibir Resultado        =====
def mostrar_resultado(numero1, numero2, operacao, resultado):
    print(f"{numero1} {simbolo_operacao(operacao)} {numero2} = {resultado}")