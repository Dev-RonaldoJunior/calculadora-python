print("===== CALCULADORA BASICA =====")
print("=====      1ª Versão     =====")

#entrada dos valores a ser calculados
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

#Escolha da função
print("\nEscolha uma operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operacao = input("Opção: ")

#Função de Soma
if operacao == "1":
    resultado = numero1 + numero2
    print("Resultado:", resultado)

#Função de Subtração
elif operacao == "2":
    resultado = numero1 - numero2
    print("Resultado:", resultado)

#Função de multiplicação
elif operacao == "3":
    resultado = numero1 * numero2
    print("Resultado:", resultado)

#Função de divisão
elif operacao == "4":
    resultado = numero1 / numero2
    print("Resultado:", resultado)

#msg de erro
else:
    print("Opção inválida!")