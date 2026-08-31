print("===== CALCULADORA BASICA =====")
print("=====        V1.1        =====")

while True:

    #Escolha da função
    print("\nEscolha uma operação:")
    print("0 - Fechar Calculadora")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    operacao = input("Opção: ")

    #Fechar calculadora
    if operacao == "0":
        break

    #input dos valores a serem calculados
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    #Função de Soma
    if operacao == "1":
        resultado = numero1 + numero2
        print("Resultado:", resultado)

    #Função de Subtração
    elif operacao == "2":
        resultado = numero1 - numero2
        print("Resultado:", resultado)

    #Função de Multiplicação
    elif operacao == "3":
        resultado = numero1 * numero2
        print("Resultado:", resultado)

    #Função de Divisão
    elif operacao == "4":
        resultado = numero1 / numero2
        print("Resultado:", resultado)

    #msg de erro
    else:
        print("Opção inválida!")