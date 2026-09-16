#==============================IMPORT==============================
from operacoes import OPERACOES_CALCULO
#==============================FUNÇÕES==============================

#=====        Formatar Resultado        =====
def formatar_resultado(item):

    if OPERACOES_CALCULO[item["operacao"]]["formato"] == "porcentagem":

        return (
            f"{item['numero1']:.10g}"
            f"{OPERACOES_CALCULO[item['operacao']]['simbolo']} de "
            f"{item['numero2']:.10g} = "
            f"{item['resultado']:.10g}"
        )

    elif OPERACOES_CALCULO[item["operacao"]]["formato"] == "raiz":

        return (
            f"{OPERACOES_CALCULO[item['operacao']]['simbolo']}"
            f"{item['numero1']:.10g} = "
            f"{item['resultado']:.10g}"
        )

    else:

        return (
            f"{item['numero1']:.10g} "
            f"{OPERACOES_CALCULO[item['operacao']]['simbolo']} "
            f"{item['numero2']:.10g} = "
            f"{item['resultado']:.10g}"
        )

#=====        Exibir Resultado        =====

def mostrar_resultado(numero1, numero2, operacao, resultado):

    item = {
        "numero1": numero1,
        "numero2": numero2,
        "operacao": operacao,
        "resultado": resultado
    }

    resultado_formatado = formatar_resultado(item)

    print(resultado_formatado)

    return resultado_formatado
