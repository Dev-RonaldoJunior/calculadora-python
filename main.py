#==============================IMPORT==============================
import calculos, historico, entradas, validacoes, apresentacao

#==============================CONSTANTE==============================
OPERACOES_CALCULO = {
    "1": ("Soma", calculos.somar),
    "2": ("Subtração", calculos.subtrair),
    "3": ("Multiplicação", calculos.multiplicar),
    "4": ("Divisão", calculos.dividir),
    "5": ("Porcentagem", calculos.porcentagem),
    "6": ("Potência", calculos.potencia)
}

#==============================FUNÇÕES==============================                    
#=====        Calcular        =====
def realizar_calculo(operacao, numero1, numero2):
    return OPERACOES_CALCULO[operacao][1](numero1, numero2)

#=====        Mostrar Menu        =====
def mostrar_menu():
    print("\n0 - Encerrar Calculadora")
    for numero, dados in OPERACOES_CALCULO.items():
        print(f"{numero} - {dados[0]}")
    print("7 - Historico")

#=====        Função Principal       =====
def main():
    #==============================APRESENTAÇÃO==============================
    print("\n===== CALCULADORA BASICA =====")
    print("=====        V1.37.0       =====")

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
        if not validacoes.validar_operacao(operacao, OPERACOES_CALCULO):
            print("\nOpção inválida!")
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
        resultado_final = apresentacao.mostrar_resultado(numero1, numero2, operacao, resultado)
        
        #==============================ADICIONAR AO HISTÓRICO==============================
        lista_historico.append(resultado_final)

#=======================================================================================================================================================#
#=================================================================CALCULADORA FUNCIONANDO===============================================================#
#=======================================================================================================================================================#

if __name__ == "__main__":
    main()
