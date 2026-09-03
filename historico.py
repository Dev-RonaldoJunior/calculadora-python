#=====        Mostrar Histórico       =====
def mostrar_historico(historico):
    if not historico:
        print("\nNenhum cálculo realizado.")
    
    else:
        for item in historico:
            print(item)

#=====        Limpar Histórico        =====
def limpar_historico(historico):
    print("\nTem certeza que deseja apagar o histórico da calculadora?")
    print("S para sim e N para Não")
    

    while True:
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
    #==============================SUB MENU==============================
    print("\n1 - Ver histórico")
    print("2 - Limpar Histórico")

    while True:

        #==============================INPUT DA OPÇÃO DO HISTÓRICO==============================
        operacao2 = input("\nOpção: ")

        if operacao2 == "1":
            mostrar_historico(historico)
            break
        elif operacao2 =="2":
            limpar_historico(historico)
            break
        else:
            print("Opção inválida!")