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