#=====        Input de Número        =====
def input_numero(mensagem):

    while True:
        try:
            numero = float(input(mensagem))
            return numero

        except ValueError:
            print("\nValor digitado invalido!")
            print("Digite apenas números.")

#=====        Input de Confirmarção para apagar historico        =====
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
            print("Opção inválida!")