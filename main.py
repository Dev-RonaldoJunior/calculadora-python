#==============================IMPORT==============================
import calculos, historico, entradas, validacoes, menu

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
#=====        Calcular        =====
def realizar_calculo(operacao, numero1, numero2):
    return OPERACOES_CALCULO[operacao](numero1, numero2)

#=====        Símbolo da Operação        =====
def simbolo_operacao(operacao):
    return SIMBOLOS_OPERACOES[operacao]

#=====        Exibir Resultado        =====
def mostrar_resultado(numero1, numero2, operacao, resultado):
    print(f"{numero1} {simbolo_operacao(operacao)} {numero2} = {resultado}")

#=====        Função Principal       =====
def main():
    #==============================APRESENTAÇÃO==============================
    print("\n===== CALCULADORA BASICA =====")
    print("=====        V3.5        =====")

    #==============================LISTA PARA HISTÓRICO DE CALCULOS==============================
    lista_historico = []

    #==============================LOOP==============================
    while True:

        menu.mostrar_menu()

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
        if not validacoes.validar_operacao(operacao, OPERACOES_VALIDAS):
            print("\nOpção inválida!")
            continue

        #==============================INPUT DOS NÚMEROS==============================
        numero1 = entradas.input_numero1()
        numero2 = entradas.input_numero2()

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
