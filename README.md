# 🧮 Calculadora Básica em Python

Projeto desenvolvido em Python com o objetivo de praticar lógica de programação, funções, modularização, validação de entradas, organização de código e controle de versões utilizando Git e GitHub.

---

## 📌 Sobre o Projeto

A **Calculadora Básica em Python** é uma aplicação executada pelo terminal que permite realizar operações matemáticas e manter um histórico dos cálculos realizados durante a execução.

O projeto foi desenvolvido de forma incremental, adicionando novas funcionalidades e reorganizando sua estrutura conforme a evolução do código.

Atualmente, a calculadora possui:

* ➕ Soma
* ➖ Subtração
* ✖️ Multiplicação
* ➗ Divisão
* 📊 Porcentagem
* 📋 Histórico de cálculos
* 🗑️ Limpeza do histórico
* ✅ Validação de operações
* 🔢 Validação de números
* 🚫 Tratamento de divisão por zero

---

## 📐 Versionamento

Este projeto utiliza **Semantic Versioning (SemVer)** no formato:

```text
MAJOR.MINOR.PATCH
```

* **MAJOR** → alterações grandes ou incompatíveis.
* **MINOR** → novas funcionalidades compatíveis.
* **PATCH** → correções de bugs e pequenas correções.

Exemplo:

```text
1.27.0
│ │  │
│ │  └── PATCH
│ └───── MINOR
└─────── MAJOR
```

---

## 🗂️ Estrutura do Projeto

```text
calculadora-python/
│
├── main.py
├── calculos.py
├── historico.py
├── entradas.py
├── validacoes.py
├── apresentacao.py
├── README.md
├── .gitignore
└── LICENSE
```

### `main.py`

Responsável pelo fluxo principal da aplicação:

* Exibição do menu;
* Controle do loop principal;
* Seleção das operações;
* Integração entre os módulos;
* Execução dos cálculos;
* Controle do histórico.

### `calculos.py`

Contém as funções responsáveis exclusivamente pelos cálculos matemáticos:

* `somar()`
* `subtrair()`
* `multiplicar()`
* `dividir()`
* `porcentagem()`

### `historico.py`

Responsável pelo gerenciamento do histórico:

* Exibição dos cálculos;
* Limpeza do histórico;
* Menu do histórico.

### `entradas.py`

Responsável pela entrada dos números e tratamento de valores inválidos.

### `validacoes.py`

Responsável pelas validações das operações escolhidas pelo usuário.

### `apresentacao.py`

Responsável pela apresentação dos resultados e pelos símbolos das operações.

---

## ⚙️ Funcionalidades

### Operações matemáticas

A calculadora permite realizar:

```text
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
5 - Porcentagem
```

A operação de porcentagem calcula:

```text
X% de Y
```

Exemplo:

```text
15% de 200 = 30
```

### Histórico

Os cálculos realizados durante a execução são armazenados em uma lista e podem ser consultados através da opção:

```text
6 - Histórico
```

O histórico permite:

```text
1 - Ver histórico
2 - Limpar Histórico
```

A limpeza do histórico possui confirmação antes da exclusão dos dados.

---

## 🛠️ Tecnologias

* 🐍 Python
* 💻 VS Code
* 🔀 Git
* 🐙 GitHub
* 🖥️ GitHub Desktop

---

## 📚 Histórico de Versões

### 1.27.0

* Adicionada a operação de porcentagem.
* Criada a função `porcentagem()` em `calculos.py`.
* Adicionada a opção de porcentagem ao menu principal.
* Integrada a porcentagem ao dicionário de operações.
* Adicionado o símbolo `%`.
* Criada a função `formatar_resultado()` em `apresentacao.py`.
* Adicionada formatação específica para porcentagem.
* Ajustado o armazenamento do resultado formatado no histórico.
* Mantidas as operações e funcionalidades existentes.

### 1.26.1

* Corrigida a estrutura de modularização do projeto.
* Removido o `menu.py` após revisão arquitetural.
* Restaurada a função `mostrar_menu()` no `main.py`.
* Mantida a separação de responsabilidades dos demais módulos.

### 1.26.0

* Criado o módulo `apresentacao.py`.
* Movida a função `simbolo_operacao()` para o novo módulo.
* Movida a função `mostrar_resultado()` para o novo módulo.
* Movido o dicionário `SIMBOLOS_OPERACOES` para o novo módulo.

### 1.25.0

* Criado o módulo `menu.py`.
* Separada a função responsável pelo menu em um módulo próprio.
* Posteriormente revisado e revertido na versão `1.26.1` por excesso de modularização.

### 1.24.0

* Criado o módulo `validacoes.py`.
* Movida a função `validar_operacao()` para o novo módulo.
* A lista de operações válidas passou a ser enviada como parâmetro.

### 1.23.0

* Criado o módulo `entradas.py`.
* Movidas as funções de entrada de números para o novo módulo.
* Separada a responsabilidade de entrada de dados do fluxo principal.

### 1.22.0

* Criado o módulo `historico.py`.
* Movidas as funções relacionadas ao histórico para o novo módulo.
* Separada a responsabilidade de gerenciamento do histórico.

### 1.21.0

* Criado o dicionário `OPERACOES_CALCULO`.
* Associadas as opções do menu diretamente às funções de cálculo.
* Simplificada a seleção das operações.

### 1.20.0

* Criado o dicionário `SIMBOLOS_OPERACOES`.
* Centralizada a representação dos símbolos matemáticos.

### 1.19.0

* Criada a constante `OPERACOES_VALIDAS`.
* Centralizada a lista de operações aceitas pelo programa.

### 1.18.0

* Criada a função `mostrar_resultado()`.
* Centralizada a exibição dos resultados.

### 1.17.0

* Implementada repetição do submenu do histórico em caso de opção inválida.

### 1.16.0

* Implementada repetição da confirmação de limpeza do histórico em caso de opção inválida.

### 1.15.0

* Criada a função `input_numero()`.
* Centralizada a entrada dos números.

### 1.14.0

* Criada a função `validar_operacao()`.
* Centralizada a validação da operação escolhida.

### 1.13.0

* Criada a função `menu_historico()`.
* Criado submenu específico para gerenciamento do histórico.

### 1.12.0

* Criada a função `main()`.
* Movido o loop principal para a função principal.
* Adicionado `if __name__ == "__main__":`.
* Preparado o projeto para facilitar testes.

### 1.11.0

* Criada a função `realizar_calculo()`.
* Criada a função `simbolo_operacao()`.
* Melhorada a organização da execução dos cálculos.
* Corrigido o nome da função `imput_numero()` para `input_numero()`.

### 1.10.0

* Separadas as operações matemáticas em funções.
* Criado o arquivo `calculos.py`.
* Adicionado o import do módulo de cálculos.

### 1.9.0

* Implementado tratamento de entradas inválidas para números.

### 1.8.0

* Implementada confirmação antes de apagar o histórico.
* Adicionadas opções de confirmação e cancelamento.

### 1.7.0

* Implementada limpeza do histórico.

### 1.6.0

* Adicionada visualização do histórico.
* Criada mensagem para histórico vazio.

### 1.5.0

* Criado o histórico de cálculos.

### 1.4.0

* Implementado tratamento de divisão por zero.

### 1.3.0

* Implementado tratamento de opções inválidas.

### 1.2.0

* Implementado menu principal.
* Adicionada opção para encerrar a calculadora.

### 1.1.0

* Implementadas as operações básicas:

  * Soma
  * Subtração
  * Multiplicação
  * Divisão

### 1.0.0

* Criada a primeira versão funcional da calculadora.

---

## 🚀 Próximas Versões

O projeto continuará evoluindo de forma incremental, priorizando melhorias que contribuam para o aprendizado e para a qualidade do código.

As próximas funcionalidades serão definidas conforme a evolução do projeto.

---

## ▶️ Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/Dev-RonaldoJunior/calculadora-python.git
```

### 2. Acesse a pasta do projeto

```bash
cd calculadora-python
```

### 3. Execute o programa

```bash
python main.py
```

---

## 👨‍💻 Autor

**Ronaldo José da Silva Junior**

Projeto desenvolvido para estudos, prática de programação em Python e construção de portfólio profissional.
