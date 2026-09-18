#==============================IMPORT==============================
import calculos

#==============================CONSTANTE==============================
OPERACOES_CALCULO = {
    "1": {
        "nome": "Soma",
        "simbolo": "+",
        "funcao": calculos.somar,
        "formato": "soma",
        "quantidade_numeros": 2
    },
    "2": {
        "nome": "Subtração",
        "simbolo": "-",
        "funcao": calculos.subtrair,
        "formato": "subtrair",
        "quantidade_numeros": 2
    },
    "3": {
        "nome": "Multiplicação",
        "simbolo": "x",
        "funcao": calculos.multiplicar,
        "formato": "multiplicar",
        "quantidade_numeros": 2
    },
    "4": {
        "nome": "Divisão",
        "simbolo": "÷",
        "funcao": calculos.dividir,
        "formato": "dividir",
        "quantidade_numeros": 2
    },
    "5": {
        "nome": "Porcentagem",
        "simbolo": "%",
        "funcao": calculos.porcentagem,
        "formato": "porcentagem",
        "quantidade_numeros": 2
    },
    "6": {
        "nome": "Potência",
        "simbolo": "^",
        "funcao": calculos.potencia,
        "formato": "potencia",
        "quantidade_numeros": 2
    },

    "7": {
        "nome": "Raiz Quadrada",
        "simbolo": "√",
        "funcao": calculos.raiz,
        "formato": "raiz",
        "quantidade_numeros": 1
    },

    "8": {
        "nome": "Módulo",
        "simbolo": "mod",
        "funcao": calculos.modulo,
        "formato": "modulo",
        "quantidade_numeros": 2
    },

    "9": {
        "nome": "Fatorial",
        "simbolo": "!",
        "funcao": calculos.fatorial,
        "formato": "fatorial",
        "quantidade_numeros": 1
    }
}