#=====        Mostrar Histórico       =====
def mostrar_historico(historico):
    if not historico:
        print("\nNenhum cálculo realizado.")
    
    else:
        for item in historico:
            print(item)

#=====        Limpar Histórico        =====
def limpar_historico(historico):

    if not historico:
        print("\nNenhum cálculo para apagar.")
        return
    
    while True:
        print("\nTem certeza que deseja apagar o histórico da calculadora?")
        print("S para Sim e N para Não")

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

    while True:
        #==============================SUB MENU==============================
        print("\n1 - Ver histórico")
        print("2 - Limpar Histórico")
        print("0 - Voltar")

        #==============================INPUT DA OPÇÃO DO HISTÓRICO==============================
        operacao2 = input("\nOpção: ")

        if operacao2 == "1":
            mostrar_historico(historico)
        elif operacao2 == "2":
            limpar_historico(historico)
        elif operacao2 == "0":
            break
        else:
            print("Opção inválida!")