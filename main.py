#==============================IMPORT MODULADO==============================
import calculos

#==============================APRESENTAÇÃO==============================
print("\n===== CALCULADORA BASICA =====")
print("=====        V1.7        =====")

#==============================LISTA COM HISTÓRICO DE CALCULOS==============================
historico = []

#==============================LOOP==============================
while True:
    #==============================FUNÇÕES DISPONIVEIS==============================
    print("\nEscolha uma operação:")
    print("0 - Fechar Calculadora")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Histórico")

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
            #==============================HISTÓRICO VAZIO==============================
            if not historico:
                print("\nNenhum cálculo realizado.")

            #==============================LIMPANDO HISTÓRICO==============================
            else:
                for item in historico:
                    print(item)
            
            continue

        #==============================APAGAR HISTÓRICO==============================
        elif operacao2 == "2":
            #==============================SUB MENU DE CONFIRMAÇÃO==============================
            print("\nTem certeza que deseja apagar o histórico da calculadora?")
            print("S para sim e N para Não")

            operacao3 = input("Opção: ")

            operacao3 = operacao3.upper()

            #==============================CONFIRMAÇÂO POSITIVA==============================
            if operacao3 == "S":
                historico.clear()
                print("Histórico Limpo.")
                continue

            #==============================CONFIRMAÇÃO NEGATIVA==============================
            elif operacao3 == "N":
                print("\nHistórico não apagado")
                continue

            #==============================CONFIRMAÇÃO INVALIDA==============================
            else:
                print("\nOpção inválida!")
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