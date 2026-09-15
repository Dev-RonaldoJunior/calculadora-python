#==============================IMPORT==============================
import calculos

#==============================CONSTANTE==============================
OPERACOES_CALCULO = {
    "1": {
        "nome": "Soma",
        "simbolo": "+",
        "funcao": calculos.somar
    },
    "2": {
        "nome": "Subtração",
        "simbolo": "-",
        "funcao": calculos.subtrair
    },
    "3": {
        "nome": "Multiplicação",
        "simbolo": "x",
        "funcao": calculos.multiplicar
    },
    "4": {
        "nome": "Divisão",
        "simbolo": "÷",
        "funcao": calculos.dividir
    },
    "5": {
        "nome": "Porcentagem",
        "simbolo": "%",
        "funcao": calculos.porcentagem
    },
    "6": {
        "nome": "Potência",
        "simbolo": "^",
        "funcao": calculos.potencia
    }
}