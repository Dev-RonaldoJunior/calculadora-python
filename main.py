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
    
    operacao = input("Opção: ")
    
    operacao = operacao.upper()

    #Positivo
    if operacao == "S":
        historico.clear()
        print("Histórico Limpo.")

    #Negativo
    elif operacao == "N":
        print("\nHistórico não apagado")

    #Invalido
    else:
        print("\nOpção inválida!")

#==============================APRESENTAÇÃO==============================
print("\n===== CALCULADORA BASICA =====")
print("=====        V1.8        =====")

#==============================LISTA COM HISTÓRICO DE CALCULOS==============================
historico = []

#==============================LOOP==============================
while True:

    mostrar_menu()

    #==============================IMPUT DA OPÇÃO DE FUNÇÃO==============================
    operacao = input("\nOpção: ")

    #==============================FECHAR A CALCULADORA==============================
    if operacao == "0":
        print("\nCalculadora encerrada")
        break

    #==============================FUNÇÃO DO HISTÓRICO==============================
    elif operacao == "5":

        #==============================SUB MENU==============================
        print("\n1 - Ver histórico")
        print("2 - Limpar Histórico")

        #==============================IMPUT da OPÇÃO DO HISTÓRICO==============================
        operacao2 = input("\nOpção: ")

        #==============================VISUALIZAR HISTÓRICO==============================
        if operacao2 == "1":
            mostrar_historico(historico)
            continue

        #==============================APAGAR HISTÓRICO==============================
        elif operacao2 == "2":
            #==============================SUB MENU DE CONFIRMAÇÃO==============================
            limpar_historico(historico)
            continue

        #==============================SUB MENU DE CONFIRMAÇÃO OPÇÃO INVALIDA==============================
        else:
            print("\nOpção inválida!")
            continue        

    #==============================IMPUT DOS VALORES A SEREM CALCULADOS==============================(COM TRATAMENTO DE ERROS "try e except")
    try:
        numero1 = float(input("\nDigite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))

    except:
        print("\nValor digitado invalido")
        print("Digite apenas numeros")
        continue

    #==============================ADIÇÃO==============================
    if operacao == "1":
        resultado = calculos.somar(numero1, numero2)
        print("Resultado:", resultado)
        historico.append(f"{numero1} + {numero2} = {resultado}")

    #==============================SUBTRAÇÃO==============================
    elif operacao == "2":
        resultado = calculos.subtrair(numero1, numero2)
        print("Resultado:", resultado)
        historico.append(f"{numero1} - {numero2} = {resultado}")

    #==============================MULTIPLICAÇÃO==============================
    elif operacao == "3":
        resultado = calculos.multiplicar(numero1, numero2)
        print("Resultado:", resultado)
        historico.append(f"{numero1} x {numero2} = {resultado}")

    #==============================DIVISÃO==============================
    elif operacao == "4":
        if numero2 == 0:
            print("\nNão é possível dividir por zero")
        else:    
            resultado = calculos.dividir(numero1, numero2)
            print("Resultado:", resultado)
            historico.append(f"{numero1} ÷ {numero2} = {resultado}")

    #==============================MSG ERRO==============================
    else:
        print("\nOpção inválida!")