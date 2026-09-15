#=====        Input de Número        =====
def input_numero(mensagem):

    while True:
        try:
            numero = float(input(mensagem))
            return numero

        except ValueError:
            print("\nValor digitado invalido!")
            print("Digite apenas números.")

#=====        Input de Confirmação       =====
def confirmar_acao(mensagem):

    while True:
        print(f"\n{mensagem}")
        print("S para Sim e N para Não")

        operacao = input("Opção: ").upper()

        #Positivo
        if operacao == "S":
            return True

        #Negativo
        elif operacao == "N":
            return False

        #Invalido
        else:
            print("\nOpção inválida!")

#=====        Input de Opção       =====
def input_opcao(mensagem, opcoes_validas):

    while True:
        opcao = input(mensagem)

        if opcao in opcoes_validas:
            return opcao

        print("\nOpção inválida!")
