# 🧮 Calculadora Básica em Python

Projeto desenvolvido em Python com o objetivo de praticar lógica de programação, estruturas de repetição, condicionais, tratamento de erros, listas, funções e modularização.

## 📌 Sobre o projeto

Esta é uma calculadora executada pelo terminal, desenvolvida de forma incremental, com novas funcionalidades adicionadas a cada versão.

O projeto faz parte do meu portfólio de estudos em programação.

## 🚀 Funcionalidades

* ➕ Soma

* ➖ Subtração

* ✖️ Multiplicação

* ➗ Divisão

* 🛑 Tratamento de divisão por zero

* ⚠️ Tratamento de entradas inválidas

* 📋 Histórico de cálculos

* 🗑️ Limpeza do histórico

* ✅ Confirmação antes de apagar o histórico

* 📦 Operações matemáticas separadas em um módulo

* 🔧 Funções para organização do menu e histórico

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

Responsável pelo funcionamento principal da calculadora, incluindo:

* Menu de opções

* Entrada dos dados

* Histórico

* Tratamento de erros

* Controle do programa

* Funções para organização do menu e histórico

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

### V1.8

* Criação da função `mostrar_menu()`

* Criação da função `mostrar_historico()`

* Criação da função `limpar_historico()`

* Utilização de parâmetros nas funções relacionadas ao histórico

* Melhor organização do código

* Redução de código repetido

* Separação das responsabilidades através de funções

### V1.7

* Operações matemáticas separadas no arquivo `calculos.py`

* Criação de funções para soma, subtração, multiplicação e divisão

* Utilização de `import` para acessar o módulo de cálculos

* Organização do código em arquivos separados

* Manutenção do histórico de cálculos

* Tratamento de divisão por zero

* Tratamento de entradas inválidas

### V1.6

* Separação das operações matemáticas em funções

* Criação do módulo `calculos.py`

### V1.5

* Confirmação antes de limpar o histórico

* Opções para confirmar ou cancelar a exclusão

### V1.4

* Opção para limpar o histórico

* Submenu de histórico

### V1.3

* Visualização do histórico

* Mensagem quando não existem cálculos registrados

### V1.2

* Criação do histórico de cálculos

### V1.1

* Tratamento de entradas inválidas

* Tratamento de divisão por zero

### V1.0

* Soma

* Subtração

* Multiplicação

* Divisão

* Menu de operações

* Encerramento da calculadora

## 🔮 Futuras atualizações

* [ ] Melhorar a formatação dos resultados

* [ ] Adicionar novas operações matemáticas

* [ ] Permitir operações com mais de dois números

* [ ] Melhorar o sistema de histórico

* [ ] Criar uma interface gráfica

* [ ] Adicionar testes automatizados

## ▶️ Como executar

É necessário ter o Python instalado.

Clone o repositório, abra a pasta no VS Code e execute:

```bash
python main.py
```

## 👨‍💻 Autor

**Ronaldo José da Silva Junior**

Projeto desenvolvido para estudos e construção de portfólio.
