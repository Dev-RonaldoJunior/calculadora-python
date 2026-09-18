#==============================IMPORT==============================
from operacoes import OPERACOES_CALCULO
#==============================FUNÇÕES==============================

#=====        Formatar Resultado        =====
def formatar_resultado(item):
    #=====        Tratamento para Porcentagem     =====
    if OPERACOES_CALCULO[item["operacao"]]["formato"] == "porcentagem":
        return (
            f"{item['numero1']:.10g}"
            f"{OPERACOES_CALCULO[item['operacao']]['simbolo']} de "
            f"{item['numero2']:.10g} = "
            f"{formatar_preciso(item['resultado'])}"
        )

    #=====        Tratamento para Raiz     =====
    elif OPERACOES_CALCULO[item["operacao"]]["formato"] == "raiz":
        return (
            f"{OPERACOES_CALCULO[item['operacao']]['simbolo']}"
            f"{item['numero1']:.10g} = "
            f"{formatar_preciso(item['resultado'])}"
        )

    #=====        Tratamento para Fatorial     =====
    elif OPERACOES_CALCULO[item["operacao"]]["formato"] == "fatorial":
        return(
            f"{item['numero1']:.10g}"
            f"{OPERACOES_CALCULO[item['operacao']]['simbolo']} = "
            f"{formatar_preciso(item['resultado'])}"
        )
 
    #=====        Tratamento para calculos basicos     =====
    else:
        return (
            f"{item['numero1']:.10g} "
            f"{OPERACOES_CALCULO[item['operacao']]['simbolo']} "
            f"{item['numero2']:.10g} = "
            f"{formatar_preciso(item['resultado'])}"
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

#=====        Formatar numero        =====
def formatar_preciso(numero):
    if isinstance(numero, float):
        return f"{numero:.10g}"
    
    num_str = str(abs(numero))
    tamanho = len(num_str)
    
    if tamanho > 10:
        sinal = "-" if numero < 0 else ""
        primeiro_digito = num_str[0]
        restante = num_str[1:10].rstrip('0') 
        expoente = tamanho - 1
        
        ponto = f".{restante}" if restante else ""
        return f"{sinal}{primeiro_digito}{ponto}e+{expoente}"
    
    return str(numero)