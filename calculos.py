#=====        Função de Adição        =====
def somar(n1, n2):
    return n1 + n2

#=====        Função de Subtração        =====
def subtrair(n1, n2):
    return n1 - n2

#=====        Função de Multiplicação        =====
def multiplicar(n1, n2):
    return n1 * n2

#=====        Função de Divisão        =====
def dividir(n1, n2):
    return n1 / n2

#=====        Função de Porcentagem        =====
def porcentagem(n1, n2):
    return n1 * n2 / 100

#=====        Função de Potência       =====
def potencia(n1, n2):
    pdn = n2
    res = 1
    while True:
        if pdn > 0:
            resut = res * n1
            res = resut
            pdn -= 1
        else:
            return res