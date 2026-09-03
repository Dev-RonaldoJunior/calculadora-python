#==============================IMPORT==============================
import calculos, historico

#==============================CONSTANTE==============================
OPERACOES_VALIDAS = ["1", "2", "3", "4"]

SIMBOLOS_OPERACOES = {
    "1": "+",
    "2": "-",
    "3": "x",
    "4": "÷"
}

OPERACOES_CALCULO = {
    "1": calculos.somar,
    "2": calculos.subtrair,
    "3": calculos.multiplicar,
    "4": calculos.dividir
}

#==============================FUNÇÕES==============================
#=====        Mostrar Menu        =====
def mostrar_menu():
    print("\nEscolha uma operação:")
    print("0 - Fechar Calculadora")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Histórico")
                    
#=====        Input do Número1        =====
def input_numero1():
    while True:
        try:
            numero1 = float(input("\nDigite o primeiro número: "))
            return numero1

        except:
            print("\nValor digitado invalido!")
            print("Digite apenas numero.")
        
#=====        Input do Número2        =====
def input_numero2():
    while True:
        try:
            numero2 = float(input("\nDigite o segundo número: "))
            return numero2
        except:
            print("\nValor digitado invalido!")
            print("Digite apenas numero.")

#=====        Calcular        =====
def realizar_calculo(operacao, numero1, numero2):
    return OPERACOES_CALCULO[operacao](numero1, numero2)

#=====        Símbolo da Operação        =====
def simbolo_operacao(operacao):
    return SIMBOLOS_OPERACOES[operacao]

#=====        Validar Operação        =====
def validar_operacao(operacao):
    if operacao in OPERACOES_VALIDAS:
        return True

    else:
        return False

#=====        Exibir Resultado        =====
def mostrar_resultado(numero1, numero2, operacao, resultado):
    print(f"{numero1} {simbolo_operacao(operacao)} {numero2} = {resultado}")

#=====        Função Principal       =====
def main():
    #==============================APRESENTAÇÃO==============================
    print("\n===== CALCULADORA BASICA =====")
    print("=====        V3.1        =====")

    #==============================LISTA PARA HISTÓRICO DE CALCULOS==============================
    lista_historico = []

    #==============================LOOP==============================
    while True:

        mostrar_menu()

        #==============================INPUT DA OPÇÃO DE FUNÇÃO==============================
        operacao = input("\nOpção: ")

        #==============================FECHAR A CALCULADORA==============================
        if operacao == "0":
            print("\nCalculadora encerrada")
            break

        #==============================HISTÓRICO==============================
        elif operacao == "5":
            historico.menu_historico(lista_historico)
            continue

        #==============================VERIFICAÇÃO DA OPERAÇÃO==============================
        if not validar_operacao(operacao):
            print("\nOpção inválida!")
            continue

        #==============================INPUT DOS NÚMEROS==============================
        numero1 = input_numero1()
        numero2 = input_numero2()

        #==============================TRATAMENTO DE DIVISÃO POR ZERO==============================
        if operacao == "4" and numero2 == 0:
            print("\nNão é possível dividir por zero")
            continue

        #==============================REALIZAR CÁLCULO==============================
        resultado = realizar_calculo(operacao, numero1, numero2)

        #==============================EXIBIR RESULTADO==============================
        mostrar_resultado(numero1, numero2, operacao, resultado)

        #==============================ADICIONAR AO HISTÓRICO==============================
        simbolo = simbolo_operacao(operacao)
        lista_historico.append(f"{numero1} {simbolo} {numero2} = {resultado}")

#=======================================================================================================================================================#
#=================================================================CALCULADORA FUNCIONANDO===============================================================#
#=======================================================================================================================================================#

if __name__ == "__main__":
    main()
