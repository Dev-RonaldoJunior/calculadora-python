#==============================IMPORT==============================
import historico, entradas, apresentacao, operacoes

#==============================FUNÇÕES==============================
#=====        Calcular        =====
def realizar_calculo(operacao, numero1, numero2):
    return operacoes.OPERACOES_CALCULO[operacao]["funcao"](numero1, numero2)

#=====        Mostrar Menu        =====
def mostrar_menu():
    print("\n0 - Encerrar Calculadora")

    for numero, dados in operacoes.OPERACOES_CALCULO.items():
        print(f"{numero} - {dados['nome']}")

    print("7 - Historico")

#=====        Função Principal       =====
def main():

    #==============================APRESENTAÇÃO==============================
    print("\n===== CALCULADORA BASICA =====")

    #==============================LISTA PARA HISTÓRICO DE CALCULOS==============================
    lista_historico = []

    #==============================OPÇÕES DO MENU==============================
    opcoes_menu = ["0", *operacoes.OPERACOES_CALCULO.keys(), "7"]

    #==============================LOOP==============================
    while True:

        mostrar_menu()

        #==============================INPUT DA OPÇÃO DE FUNÇÃO==============================
        operacao = entradas.input_opcao("Opção: ", opcoes_menu)

        #==============================FECHAR A CALCULADORA==============================
        if operacao == "0":
            print("\nCalculadora encerrada")
            break

        #==============================HISTÓRICO==============================
        elif operacao == "7":
            historico.menu_historico(lista_historico)
            continue

        #==============================INPUT DOS NÚMEROS==============================
        numero1 = entradas.input_numero("\nDigite o primeiro número: ")
        numero2 = entradas.input_numero("Digite o segundo número: ")

        #==============================REALIZAR CÁLCULO==============================
        try:
            resultado = realizar_calculo(operacao, numero1, numero2)

        except ZeroDivisionError as erro:
            print(f"\n{erro}")
            continue

        #==============================EXIBIR RESULTADO==============================
        resultado_final = apresentacao.mostrar_resultado(
            numero1,
            numero2,
            operacao,
            resultado
        )

        #==============================ADICIONAR AO HISTÓRICO==============================
        lista_historico.append(resultado_final)

#=======================================================================================================================================================#
#=================================================================CALCULADORA FUNCIONANDO===============================================================#
#=======================================================================================================================================================#

if __name__ == "__main__":
    main()

