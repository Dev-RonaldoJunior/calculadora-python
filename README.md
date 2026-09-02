# 🧮 Calculadora Básica em Python

Projeto desenvolvido para praticar conceitos de programação em Python, como lógica de programação, estruturas de repetição, condicionais, tratamento de erros, listas, funções e modularização.

## 📌 Sobre o projeto

Uma calculadora executada pelo terminal, desenvolvida de forma incremental durante meus estudos de Python e utilizada como parte do meu portfólio.

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
* Operações matemáticas separadas em módulo
* Funções para organização do código
* Função `main()`
* Menu de histórico separado em função própria
* Validação das operações matemáticas
* Entrada dos números separada em funções próprias

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

Responsável pelo fluxo principal da calculadora, menus, entrada de dados, histórico, tratamento de erros e execução do programa.

### `calculos.py`

Contém as funções responsáveis pelas operações matemáticas:

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

* Tratamento de valores inválidos
* Tratamento de divisão por zero

### V1.2

* Criação do histórico de cálculos

### V1.3

* Visualização do histórico
* Mensagem para histórico vazio

### V1.4

* Limpeza do histórico
* Criação do submenu de histórico

### V1.5

* Confirmação antes de limpar o histórico
* Opções de confirmação ou cancelamento

### V1.6

* Operações matemáticas separadas no arquivo `calculos.py`
* Criação das funções de soma, subtração, multiplicação e divisão
* Importação do módulo `calculos`
* Separação do projeto em arquivos

### V1.7

* Criação da função `mostrar_menu()`
* Organização do menu em uma função própria
* Melhoria na organização do código

### V1.8

* Criação das funções `mostrar_historico()` e `limpar_historico()`
* Organização das funções relacionadas ao histórico
* Histórico passado como parâmetro

### V1.9

* Criação da função `input_numero()`
* Separação da entrada dos números
* Retorno dos números através da função
* Tratamento de valores inválidos

### V2.0

* Criação da função `realizar_calculo()`
* Criação da função `simbolo_operacao()`
* Validação da operação antes da entrada dos números
* Tratamento de divisão por zero
* Melhor organização do fluxo principal
* Formatação do histórico de cálculos
* Correção do nome `imput_numero()` para `input_numero()`

### V2.1

* Criação da função `main()`
* Movimentação do histórico para dentro da função principal
* Movimentação do `while` para dentro da função principal
* Implementação de `if __name__ == "__main__":`
* Melhor organização da execução do programa
* Preparação do código para futuros testes automatizados

### V2.2

* Criação da função `menu_historico()`
* Separação do submenu de histórico da função `main()`
* Organização das opções do histórico
* Histórico passado como parâmetro
* Melhoria no fluxo principal

### V2.3

* Criação da função `validar_operacao()`
* Validação das operações matemáticas
* Validação das opções de 1 a 4
* Separação da validação da função `main()`
* Melhoria na organização do código

### V2.4

* Separação da entrada do primeiro e segundo número
* Criação da função `input_numero1()`
* Criação da função `input_numero2()`
* Validação independente dos dois números
* Melhoria no tratamento de valores inválidos
* Organização da entrada de dados em funções específicas

### V2.5

* Implementação de repetição da entrada de números inválidos
* Utilização de `while` nas funções `input_numero1()` e `input_numero2()`
* Tratamento de erros através de `try/except`
* O programa continua solicitando o número até que um valor válido seja informado
* Remoção da necessidade de retornar `None` em caso de erro
* Melhoria no fluxo de entrada dos números

### V2.6

* Implementada repetição do submenu de histórico utilizando `while`
* Validação contínua das opções do submenu
* Utilização de `break` após uma opção válida
* Opção 1 chama `mostrar_historico()`
* Opção 2 chama `limpar_historico()`
* Opções inválidas não encerram mais o submenu
* Melhorado o fluxo de navegação do menu de histórico



## 🔮 Próximas versões

* Melhorar a organização da `main()`
* Melhorar a apresentação dos resultados
* Adicionar novas operações matemáticas
* Permitir cálculos com mais de dois números
* Melhorar o sistema de histórico
* Implementar testes automatizados
* Criar uma interface gráfica

## ▶️ Como executar

Certifique-se de ter o Python instalado e execute:

```bash
python main.py
```

## 👨‍💻 Autor

**Ronaldo José da Silva Junior**

Projeto desenvolvido para estudos de Python e construção de portfólio.
