print("")
print("===== CALCULADORA BASICA =====")
print("=====        V1.4        =====")

historico = []

while True:

    #Escolha da função
    print("\nEscolha uma operação:")
    print("0 - Fechar Calculadora")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Histórico")

    print("")
    operacao = input("Opção: ")
    print("")

    #Fechar calculadora
    if operacao == "0":
        break

    #Função do Hitórico
    elif operacao == "5":
        if not historico:
            print("Nenhum cálculo realizado.")

        else:
            for item in historico:
                print(item)

        continue

    #input dos valores a serem calculados
    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))

    except:
        print("")
        print("Valor digitado invalido")
        print("Digite apenas numeros")
        print("")
        continue

    #Função de Soma
    if operacao == "1":
        resultado = numero1 + numero2
        print("")
        print("Resultado:", resultado)
        historico.append(f"{numero1} + {numero2} = {resultado}")

    #Função de Subtração
    elif operacao == "2":
        resultado = numero1 - numero2
        print("")
        print("Resultado:", resultado)
        historico.append(f"{numero1} - {numero2} = {resultado}")

    #Função de Multiplicação
    elif operacao == "3":
        resultado = numero1 * numero2
        print("")
        print("Resultado:", resultado)
        historico.append(f"{numero1} x {numero2} = {resultado}")

    #Função de Divisão
    elif operacao == "4":

        if numero2 == 0:
            print("")
            print("Não é possível dividir por zero")
        else:
            resultado = numero1 / numero2
            print("")
            print("Resultado:", resultado)
            historico.append(f"{numero1} ÷ {numero2} = {resultado}")

        

    #msg de erro
    else:
        print("")
        print("Opção inválida!")