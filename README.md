# 🧮 Calculadora Básica em Python

Projeto desenvolvido para praticar conceitos de programação em Python, como lógica de programação, estruturas de repetição, condicionais, tratamento de erros, listas, funções e modularização.

## 📌 Sobre o projeto

Uma calculadora executada pelo terminal, desenvolvida de forma incremental, fazendo parte dos meus estudos e portfólio de programação.

O projeto está sendo desenvolvido por versões, adicionando novas funcionalidades e melhorando a organização do código gradualmente.

## 🚀 Funcionalidades

* Soma
* Subtração
* Multiplicação
* Divisão
* Tratamento de divisão por zero
* Tratamento de valores inválidos
* Histórico de cálculos
* Visualização do histórico
* Limpeza do histórico
* Confirmação antes de apagar o histórico
* Operações matemáticas separadas em um módulo
* Funções para organização do código
* Função principal `main()` para controlar a execução da calculadora
* Menu de histórico separado em uma função própria
* Validação das operações matemáticas

## 📂 Estrutura do projeto

```text
calculadora/
│
├── main.py
├── calculos.py
├── README.md
├── .gitignore
└── LICENSE
```

### `main.py`

Responsável pelo fluxo principal da calculadora, menus, entrada de dados, histórico, tratamento de erros e controle da execução do programa.

### `calculos.py`

Responsável pelas operações matemáticas da calculadora:

* `somar()`
* `subtrair()`
* `multiplicar()`
* `dividir()`

## 🛠️ Tecnologias utilizadas

* Python
* Visual Studio Code
* Git
* GitHub
* GitHub Desktop

## 📋 Versões

### V1.0

* Soma
* Subtração
* Multiplicação
* Divisão
* Menu de operações
* Encerramento da calculadora

### V1.1

* Tratamento de entradas inválidas
* Tratamento de divisão por zero

### V1.2

* Criação do histórico de cálculos

### V1.3

* Visualização do histórico
* Mensagem quando o histórico está vazio

### V1.4

* Limpeza do histórico
* Criação de submenu para o histórico

### V1.5

* Confirmação antes de limpar o histórico
* Opções de confirmação ou cancelamento

### V1.6

* Separação das operações matemáticas em `calculos.py`
* Criação das funções matemáticas
* Importação do módulo `calculos`
* Separação da lógica em arquivos diferentes

### V1.7

* Criação da função `mostrar_menu()`
* Organização do menu em uma função
* Melhoria na organização do código

### V1.8

* Criação da função `mostrar_historico()`
* Criação da função `limpar_historico()`
* Organização das funções relacionadas ao histórico
* Passagem do histórico como parâmetro

### V1.9

* Criação da função `input_numero()`
* Separação da entrada dos números em uma função
* Retorno dos números para o fluxo principal
* Tratamento de entradas inválidas

### V2.0

* Criação da função `realizar_calculo()`
* Criação da função `simbolo_operacao()`
* Validação da operação antes da entrada dos números
* Tratamento de divisão por zero
* Organização do fluxo principal
* Melhoria na formatação do histórico
* Correção do nome da função `input_numero()`

### V2.1

* Criação da função principal `main()`
* Movimentação do histórico para dentro da `main()`
* Movimentação do loop principal para dentro da `main()`
* Organização da execução principal do programa
* Uso de `if __name__ == "__main__":`
* Preparação da estrutura para futuros testes automatizados

### V2.2

* Criação da função `menu_historico()`
* Separação do submenu de histórico da função `main()`
* Organização das opções de visualização e limpeza do histórico
* Passagem do histórico como parâmetro para o menu
* Melhoria na organização do fluxo principal

### V2.3

* Criação da função `validar_operacao()`
* Separação da validação das operações matemáticas
* Validação das opções de `1` a `4`
* Melhoria na organização da função `main()`
* Redução da lógica diretamente dentro do fluxo principal

## 🔮 Futuras atualizações

* Melhorar a organização do `main.py`
* Melhorar a apresentação dos resultados
* Adicionar novas operações matemáticas
* Permitir cálculos com mais de dois números
* Melhorar o sistema de histórico
* Criar testes automatizados
* Criar uma interface gráfica

## ▶️ Como executar

No terminal, execute:

```bash
python main.py
```

## 👨‍💻 Autor

**Ronaldo José da Silva Junior**

Projeto desenvolvido para estudos e construção de portfólio em Python.
