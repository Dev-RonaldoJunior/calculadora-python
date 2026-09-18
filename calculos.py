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
    if n2 == 0:
        raise ZeroDivisionError("Não é possível dividir por zero")
    return n1 / n2

#=====        Função de Porcentagem        =====
def porcentagem(n1, n2):
    return n1 * n2 / 100

#=====        Função de Potência       =====
def potencia(n1, n2):
    return n1 ** n2

#=====        Função de Raiz Quadrada      =====
def raiz(n1):
    if n1 < 0:
        raise ValueError ("Não é possível calcular a raiz quadrada de um número negativo")
    return n1 ** 0.5

#=====        Função de Módulo     =====
def modulo(n1, n2):
    return n1 % n2

#=====        Função de Fatorial     =====
def fatorial(n1):
    if n1 < 0 or n1 != int(n1):
        raise ValueError("Valores negativos ou decimais não são aceitos!")
    elif n1 > 1000:
        raise ValueError("O valor máximo para o fatorial é 1000")
    elif n1 == 0 or n1 == 1:
        return 1
    else:
        resultado = 1
        for i in range(1, int(n1) + 1):
            resultado *= i
        return resultado
