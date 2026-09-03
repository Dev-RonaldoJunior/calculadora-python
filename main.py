#==============================IMPORT MODULADO==============================
import calculos

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

#=====        Mostrar Histórico       =====
def mostrar_historico(historico):
    if not historico:
        print("\nNenhum cálculo realizado.")
    
    else:
        for item in historico:
            print(item)

#=====        Limpar Histórico        =====
def limpar_historico(historico):
    print("\nTem certeza que deseja apagar o histórico da calculadora?")
    print("S para sim e N para Não")
    

    while True:
        operacao = input("Opção: ")
        
        operacao = operacao.upper()
        #Positivo
        if operacao == "S":
            historico.clear()
            print("Histórico Limpo.")
            break

        #Negativo
        elif operacao == "N":
            print("\nHistórico não apagado")
            break

        #Invalido
        else:
            print("\nOpção inválida!")

#=====        Sub Menu do Histórico        =====
def menu_historico(historico):
    #==============================SUB MENU==============================
    print("\n1 - Ver histórico")
    print("2 - Limpar Histórico")

    while True:

        #==============================INPUT DA OPÇÃO DO HISTÓRICO==============================
        operacao2 = input("\nOpção: ")

        if operacao2 == "1":
            mostrar_historico(historico)
            break
        elif operacao2 =="2":
            limpar_historico(historico)
            break
        else:
            print("Opção inválida!")
                    
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

    #==============================ADIÇÃO==============================
    if operacao == "1":
        return calculos.somar(numero1, numero2)

    #==============================SUBTRAÇÃO==============================
    elif operacao == "2":
        return calculos.subtrair(numero1, numero2)

    #==============================MULTIPLICAÇÃO==============================
    elif operacao == "3":
        return calculos.multiplicar(numero1, numero2)

    #==============================DIVISÃO==============================
    elif operacao == "4":
        return calculos.dividir(numero1, numero2)

#=====        Símbolo da Operação        =====
def simbolo_operacao(operacao):

    if operacao == "1":
        return "+"

    elif operacao == "2":
        return "-"

    elif operacao == "3":
        return "x"

    elif operacao == "4":
        return "÷"

#=====        Validar Operação        =====
def validar_operacao(operacao):
    if operacao in ["1", "2", "3", "4"]:
        return True

    else:
        return False

#=====        Função Principal       =====
def main():
    #==============================APRESENTAÇÃO==============================
    print("\n===== CALCULADORA BASICA =====")
    print("=====        V2.7        =====")

    #==============================LISTA PARA HISTÓRICO DE CALCULOS==============================
    historico = []

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
            menu_historico(historico)
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
        print("Resultado:", resultado)

        #==============================ADICIONAR AO HISTÓRICO==============================
        simbolo = simbolo_operacao(operacao)
        historico.append(f"{numero1} {simbolo} {numero2} = {resultado}")

#=======================================================================================================================================================#
#=================================================================CALCULADORA FUNCIONANDO===============================================================#
#=======================================================================================================================================================#

if __name__ == "__main__":
    main()
