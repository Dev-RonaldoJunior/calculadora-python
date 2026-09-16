#==============================IMPORT==============================
import entradas, apresentacao
#==============================FUNÇÕES==============================
#=====        Mostrar Histórico       =====
def mostrar_historico(historico):

    if not historico:
        print("\nNenhum cálculo realizado.")

    else:
        numero_item = 1

        print("\n==============================")
        print("==========HISTÓRICO===========")
        print("==============================")

        for item in historico:
            print(
                f"{numero_item}º Calculo: "
                f"{apresentacao.formatar_resultado(item)}"
            )

            numero_item += 1

        print("==============================")

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

    #==============================OPÇÕES DO MENU==============================
    opcoes_menu = ["1", "2", "0"]

    while True:

        #==============================SUB MENU==============================
        print("\n==============================")
        print("========MENU HISTÓRICO========")
        print("==============================")
        print("1 - Ver histórico")
        print("2 - Limpar Histórico")
        print("0 - Voltar")
        print("==============================")

        #==============================INPUT DA OPÇÃO DO HISTÓRICO==============================
        operacao = entradas.input_opcao("Opção: ", opcoes_menu)
        print("==============================")

        if operacao == "1":
            mostrar_historico(historico)

        elif operacao == "2":
            limpar_historico(historico)

        elif operacao == "0":
            break
