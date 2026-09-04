#==============================IMPORT==============================
import calculos, historico, entradas, validacoes, apresentacao

#==============================CONSTANTE==============================
OPERACOES_VALIDAS = ["1", "2", "3", "4", "5", "6"]

OPERACOES_CALCULO = {
    "1": calculos.somar,
    "2": calculos.subtrair,
    "3": calculos.multiplicar,
    "4": calculos.dividir,
    "5": calculos.porcentagem,
    "6": calculos.potencia
}

#==============================FUNÇÕES==============================                    
#=====        Calcular        =====
def realizar_calculo(operacao, numero1, numero2):
    return OPERACOES_CALCULO[operacao](numero1, numero2)

#=====        Mostrar Menu        =====
def mostrar_menu():
    print("\nEscolha uma operação:")
    print("0 - Fechar Calculadora")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Porcentagem")
    print('6 - Potência')
    print("7 - Histórico")

#=====        Função Principal       =====
def main():
    #==============================APRESENTAÇÃO==============================
    print("\n===== CALCULADORA BASICA =====")
    print("=====        V1.28.0        =====")

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
        elif operacao == "7":
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
        resultado_formatado = apresentacao.formatar_resultado(numero1, numero2, operacao, resultado)

        print(resultado_formatado)

        #==============================ADICIONAR AO HISTÓRICO==============================
        lista_historico.append(resultado_formatado)

#=======================================================================================================================================================#
#=================================================================CALCULADORA FUNCIONANDO===============================================================#
#=======================================================================================================================================================#

if __name__ == "__main__":
    main()
