#==============================IMPORT==============================
import historico, entradas, apresentacao, operacoes

#==============================FUNÇÕES==============================
#=====        Calcular        =====
def realizar_calculo(operacao, numeros):
    return operacoes.OPERACOES_CALCULO[operacao]["funcao"](*numeros)

#=====        Mostrar Menu        =====
def mostrar_menu():
    print("\n0 - Encerrar Calculadora")

    for numero, dados in operacoes.OPERACOES_CALCULO.items():
        print(f"{numero} - {dados['nome']}")

    print("8 - Historico")

#=====        Função Principal       =====
def main():

    #==============================APRESENTAÇÃO==============================
    print("\n===== CALCULADORA BASICA =====")

    #==============================LISTA PARA HISTÓRICO DE CALCULOS==============================
    lista_historico = []

    #==============================OPÇÕES DO MENU==============================
    opcoes_menu = ["0", *operacoes.OPERACOES_CALCULO.keys(), "8"]

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
        elif operacao == "8":
            historico.menu_historico(lista_historico)
            continue

        #==============================INPUT DOS NÚMEROS==============================
        quantidade_numeros = operacoes.OPERACOES_CALCULO[operacao]["quantidade_numeros"]

        numeros = []

        for numero in range(quantidade_numeros):

            if quantidade_numeros == 1:
                mensagem = "\nDigite o número: "

            else:
                if numero == 0:
                    mensagem = "\nDigite o primeiro número: "
                else:
                    mensagem = "Digite o segundo número: "

            numeros.append(entradas.input_numero(mensagem))

        #==============================REALIZAR CÁLCULO==============================
        try:
            resultado = realizar_calculo(operacao, numeros)

        except ZeroDivisionError as erro:
            print(f"\n{erro}")
            continue

        except ValueError as erro:
            print(f"\n{erro}")
            continue

        #==============================EXIBIR RESULTADO==============================
        numero1 = numeros[0]

        if quantidade_numeros > 1:
            numero2 = numeros[1]
        else:
            numero2 = None

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