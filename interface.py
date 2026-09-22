#==============================IMPORT==============================
import tkinter as tk
import operacoes
#==============================FUNÇÕES==============================
#=====        Adiciona o Numero no Visor       =====
def adicionar_numero(numero, visor):
    visor.insert(tk.END, numero)

#=====        Adiciona o Operador no Visor       =====
def adicionar_operador(operador, visor):
    visor.insert(tk.END, operador)

#=====        Realiza o Cálculo       =====
def calcular(visor):
    expressao = visor.get()

    for operador in ["+", "-", "×", "÷", "%"]:
        if operador in expressao:
            print("Operador:", operador)

            partes = expressao.split(operador)

            numero1 = float(partes[0])
            numero2 = float(partes[1])

            print("Número 1:", numero1)
            print("Número 2:", numero2)

            for codigo, dados in operacoes.OPERACOES_CALCULO.items():
                if dados["simbolo"] == operador:
                    resultado = dados["funcao"](numero1, numero2)

                    visor.delete(0, tk.END)
                    visor.insert(tk.END, resultado)

                    break

            break

#=====        Abre o menu       =====
def abrir_menu(botao_menu):

    menu = tk.Toplevel(botao_menu)

    menu.overrideredirect(True)
    menu.configure(
        bg="#FFD700"
    )

    frame_menu = tk.Frame(
        menu,
        bg="#101010",
        bd=0
    )
    frame_menu.pack(
        padx=1,
        pady=1
    )

    opcoes = ["📜 - Histórico", "📅 - Data", "🛈 - Sobre"]

    for opcao in opcoes:
        botao = tk.Button(
            frame_menu,
            text=opcao,
            bg="#101010",
            fg="#FFFFFF",
            activebackground="#303030",
            activeforeground="#FFD700",
            font=("Arial", 11),
            relief="flat",
            bd=0,
            width=18,
            anchor="w",
            padx=10
        )

        botao.pack(
            fill="x",
            pady=1
        )

    menu.update_idletasks()

    menu.geometry(
        f"+{botao_menu.winfo_rootx() - menu.winfo_width() + botao_menu.winfo_width()}"
        f"+{botao_menu.winfo_rooty() + botao_menu.winfo_height()}"
    )

#=====        Cria a Interface Completa        =====
def iniciar_interface():
    janela = tk.Tk()

    janela.title("Calculadora")
    janela.geometry("400x550")
    janela.minsize(400, 550)
    janela.configure(bg="#202020")

    botao_calculadora = tk.Button(
        janela,
        text="Calculadora",
        bg="#202020",
        fg="#FFD700",
        font=("Arial", 12, "bold"),
        relief="flat"
    )
    botao_calculadora.grid(
        row=0,
        column=0,
        columnspan=2,
        sticky="nsew"
    )

    botao_conversor = tk.Button(
        janela,
        text="Conversor",
        bg="#202020",
        fg="#867200",
        font=("Arial", 10, "bold"),
        relief="flat"
    )
    botao_conversor.grid(
        row=0,
        column=2,
        sticky="nsew"
    )

    botao_menu = tk.Button(
        janela,
        text="☰",
        command=lambda: abrir_menu(botao_menu),
        bg="#202020",
        fg="#FFD700",
        font=("Arial", 16, "bold"),
        relief="flat"
    )
    botao_menu.grid(
        row=0,
        column=3,
        sticky="nsew"
    )

    separador = tk.Frame(
        janela,
        bg="#FFD700",
        height=1
    )
    separador.grid(
        row=0,
        column=0,
        columnspan=4,
        sticky="sew"
    )

    visor = tk.Entry(
        janela,
        font=("Courier New", 26),
        bg="#050505",
        fg="#39FF14",
        insertbackground="#39FF14",
        justify="right",
        bd=0,
        highlightthickness=0,
#        state="readonly"
        )
    visor.grid(
        row=1,
        column=0,
        columnspan=4,
        padx=15,
        pady=(10, 5),
        sticky="nsew"
        )

    for coluna in range(4):
        janela.grid_columnconfigure(
            coluna,
            weight=1,
            uniform="colunas"
        )

    janela.grid_rowconfigure(1, weight=2)

    for linha in range(2, 7):
        janela.grid_rowconfigure(linha, weight=1)

    botoes = [
        ["AC", "⌫", "%", "÷"],
        ["7", "8", "9", "×"],
        ["4", "5", "6", "-"],
        ["1", "2", "3", "+"],
        ["🧪", "0", ".", "="]
]

    operadores = ["+", "-", "×", "÷", "%"]

    for linha, botoes_linha in enumerate(botoes, start=2):
        for coluna, texto in enumerate(botoes_linha):

            if texto in operadores:
                comando = lambda texto=texto: adicionar_operador(texto, visor)
            elif texto == "=":
                comando = lambda: calcular(visor)
            elif texto in ["AC", "⌫", "🧪"]:
                comando = lambda: None
            else:
                comando = lambda texto=texto: adicionar_numero(texto, visor)

            botao = tk.Button(
                janela,
                text=texto,
                command=comando,
                bg="#101010",
                fg="#FFFFFF",
                activebackground="#303030",
                activeforeground="#FFD700",
                font=("Arial", 14, "bold"),
                relief="flat",
                bd=0
            )

            if texto in operadores or texto == "=":
                botao.configure(
                    fg="#FFD700",
                    activebackground="#303030"
                )

            if texto == "AC":
                botao.configure(
                    fg="#FFD700",
                    activebackground="#303030"
                )

            if texto == "=":
                botao.configure(
                    bg="#FFD700",
                    fg="#101010",
                    activebackground="#FFFFFF",
                    activeforeground="#101010"
                )

            if texto =="⌫":
                botao.configure(
                    fg="#FFFFFF",
                    activeforeground="#FFD700"
                )

            if texto == "🧪":
                botao.configure(
                    fg="#FFD700",
                    activebackground="#303030"
                )

            botao.grid(
                row=linha,
                column=coluna,
                padx=2,
                pady=2,
                sticky="nsew"
                )

    janela.mainloop()

#=======================================================================================================================================================#
#===========================================================Inicia a Calculadora com Interface==========================================================#
#=======================================================================================================================================================#
iniciar_interface()