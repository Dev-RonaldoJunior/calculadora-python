#==============================IMPORT==============================
from operacoes import OPERACOES_CALCULO

#==============================FUNÇÕES==============================
#=====        Formatar Resultado        =====
def formatar_resultado(numero1, numero2, operacao, resultado):
    if OPERACOES_CALCULO[operacao]["formato"] == "porcentagem":
        return f"{numero1:.10g}{OPERACOES_CALCULO[operacao]['simbolo']} de {numero2:.10g} = {resultado:.10g}"
    elif OPERACOES_CALCULO[operacao]["formato"] == "raiz":
        return f"{OPERACOES_CALCULO[operacao]['simbolo']}{numero1:.10g} = {resultado:.10g}"
    else:
        return f"{numero1:.10g} {OPERACOES_CALCULO[operacao]['simbolo']} {numero2:.10g} = {resultado:.10g}"

#=====        Exibir Resultado        =====
def mostrar_resultado(numero1, numero2, operacao, resultado):
    resultado_formatado = formatar_resultado(numero1, numero2, operacao, resultado)
    print (resultado_formatado)
    return resultado_formatado