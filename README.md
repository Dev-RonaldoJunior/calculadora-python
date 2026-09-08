# 🧮 Calculadora Básica em Python

Uma calculadora de terminal desenvolvida em Python como projeto de aprendizado e evolução prática em programação.

O projeto começou com operações matemáticas básicas e foi evoluindo gradualmente, incorporando validação de entradas, histórico de cálculos, organização modular, novas operações matemáticas e melhorias na apresentação dos resultados.

## 🚀 Funcionalidades

* ➕ Soma
* ➖ Subtração
* ✖️ Multiplicação
* ➗ Divisão
* 📊 Porcentagem
* 🔢 Potência
* 📜 Histórico de cálculos
* 🗑️ Limpeza do histórico
* ✅ Confirmação antes de apagar o histórico
* ⚠️ Validação de operações
* 🔐 Validação de entradas numéricas
* 🚫 Tratamento de divisão por zero
* 🔢 Suporte a expoentes negativos
* ✨ Formatação dos resultados para evitar zeros decimais desnecessários

## 🖥️ Demonstração

```text
===== CALCULADORA BASICA =====
=====        V1.30.0        =====

Escolha uma operação:
0 - Fechar Calculadora
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
5 - Porcentagem
6 - Potência
7 - Histórico

Opção: 6

Digite o primeiro número: 2
Digite o segundo número: 3

2 ^ 3 = 8
```

## 📂 Estrutura do projeto

```text
calculadora-python/
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

### 📄 Organização dos módulos

#### `main.py`

Responsável pelo fluxo principal da aplicação.

* Exibe o menu principal.
* Recebe a operação escolhida.
* Coordena os diferentes módulos.
* Executa os cálculos.
* Mantém o histórico durante a execução.

#### `calculos.py`

Contém as funções responsáveis pelas operações matemáticas:

* `somar()`
* `subtrair()`
* `multiplicar()`
* `dividir()`
* `porcentagem()`
* `potencia()`

#### `historico.py`

Responsável pelo gerenciamento do histórico:

* Exibição dos cálculos realizados.
* Limpeza do histórico.
* Menu de gerenciamento do histórico.
* Confirmação antes da exclusão.

#### `entradas.py`

Responsável pela entrada dos números informados pelo usuário e pelo tratamento de valores inválidos.

#### `validacoes.py`

Responsável pelas validações relacionadas às operações disponíveis na calculadora.

#### `apresentacao.py`

Responsável pela apresentação dos resultados:

* Símbolos das operações.
* Formatação dos resultados.
* Exibição dos cálculos.

## 🛠️ Tecnologias utilizadas

* **Python**
* **Git**
* **GitHub**
* **GitHub Desktop**
* **Visual Studio Code**

## 📚 Conceitos praticados

Durante o desenvolvimento do projeto foram aplicados conceitos importantes de programação em Python, incluindo:

* Variáveis
* Tipos de dados
* Operadores matemáticos
* Condicionais
* Loops
* Funções
* Listas
* Dicionários
* Tratamento de exceções
* Validação de dados
* Modularização
* Importação de módulos
* Organização de responsabilidades
* Versionamento com Git
* Semantic Versioning (SemVer)

## 📈 Evolução do projeto

O projeto foi desenvolvido de forma incremental, começando com uma calculadora simples e evoluindo conforme novos conceitos foram aprendidos.

Entre as principais evoluções estão:

**Calculadora básica → Validações → Histórico → Modularização → Porcentagem → Potência → Melhorias na apresentação**

O histórico detalhado das alterações pode ser consultado diretamente nos commits do repositório.

## 🔢 Versionamento

O projeto utiliza **Semantic Versioning (SemVer)**:

```text
MAJOR.MINOR.PATCH
```

* **MAJOR:** mudanças grandes que podem quebrar compatibilidade.
* **MINOR:** novas funcionalidades compatíveis.
* **PATCH:** correções e pequenas melhorias.

### Versão atual

**1.30.0**

Principais características da versão atual:

* Operações matemáticas básicas.
* Porcentagem.
* Potência com suporte a expoentes negativos.
* Histórico de cálculos.
* Validação de entradas.
* Organização modular.
* Formatação dos resultados.

## ▶️ Como executar

### Pré-requisitos

É necessário ter o **Python** instalado no computador.

### Clone o repositório

```bash
git clone https://github.com/Dev-RonaldoJunior/calculadora-python.git
```

### Acesse a pasta

```bash
cd calculadora-python
```

### Execute a calculadora

```bash
python main.py
```

## 💡 Exemplos

### Soma

```text
10 + 5 = 15
```

### Divisão

```text
10 ÷ 4 = 2.5
```

### Porcentagem

```text
10% de 200 = 20
```

### Potência

```text
2 ^ 3 = 8
```

### Expoente negativo

```text
2 ^ -2 = 0.25
```

## 🎯 Objetivo do projeto

O principal objetivo deste projeto é praticar programação em Python por meio do desenvolvimento incremental de uma aplicação funcional.

Além de aprender novos conceitos, o projeto também serve como exercício de:

* Organização de código.
* Separação de responsabilidades.
* Controle de versões.
* Boas práticas de desenvolvimento.
* Evolução gradual de uma aplicação.

## 👨‍💻 Autor

**Ronaldo José da Silva Junior**

Desenvolvedor de Software e Analista de Dados.

---

⭐ Projeto desenvolvido para fins de aprendizado e construção de portfólio.
