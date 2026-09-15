from operacoes import OPERACOES_CALCULO


#=====        Símbolo da Operação        =====
def simbolo_operacao(operacao):
    return OPERACOES_CALCULO[operacao]["simbolo"]

#=====        Formatar Resultado        =====
def formatar_resultado(numero1, numero2, operacao, resultado):
    if operacao == "5":
        return f"{numero1:.10g}{simbolo_operacao(operacao)} de {numero2:.10g} = {resultado:.10g}"
    else:
        return f"{numero1:.10g} {simbolo_operacao(operacao)} {numero2:.10g} = {resultado:.10g}"

#=====        Exibir Resultado        =====
def mostrar_resultado(numero1, numero2, operacao, resultado):
    resultado_formatado = formatar_resultado(numero1, numero2, operacao, resultado)
    print (resultado_formatado)
    return resultado_formatado