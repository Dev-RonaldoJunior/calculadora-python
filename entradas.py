#=====        Input de Número        =====
def input_numero(mensagem):

    while True:
        try:
            numero = float(input(mensagem))
            return numero

        except ValueError:
            print("\nValor digitado invalido!")
            print("Digite apenas números.")