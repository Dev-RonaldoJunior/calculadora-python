import entradas

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

    confirmar = entradas.confirmar_acao(
        "Tem certeza que deseja apagar o historico da calculadora?"
    )

    #Positivo
    if confirmar:
        historico.clear()
        print("\nHistórico Limpo.")

    #Negativo
    else:
        print("\nHistórico não apagado")

#=====        Sub Menu do Histórico        =====
def menu_historico(historico):

    while True:
        #==============================SUB MENU==============================
        print("\n1 - Ver histórico")
        print("2 - Limpar Histórico")
        print("0 - Voltar")

        #==============================INPUT DA OPÇÃO DO HISTÓRICO==============================
        operacao2 = input("Opção: ")

        if operacao2 == "1":
            mostrar_historico(historico)
        elif operacao2 == "2":
            limpar_historico(historico)
        elif operacao2 == "0":
            break
        else:
            print("Opção inválida!")