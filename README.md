# 🧮 Calculadora em Python

Uma calculadora desenvolvida em Python como projeto de aprendizado e evolução prática em programação.

O projeto começou como uma calculadora de terminal e foi evoluindo gradualmente, incorporando validação de entradas, histórico de cálculos, organização modular, novas operações matemáticas, melhorias na apresentação dos resultados e, atualmente, uma interface gráfica desenvolvida com Tkinter.

## 🚀 Funcionalidades

* ➕ Soma
* ➖ Subtração
* ✖️ Multiplicação
* ➗ Divisão
* 📊 Porcentagem
* 🔢 Potência
* √ Raiz quadrada
* ➗ Módulo
* ❗ Fatorial
* 📜 Histórico de cálculos
* 🗑️ Limpeza do histórico
* ✅ Confirmação antes de apagar o histórico
* 🔐 Validação de entradas numéricas
* 🚫 Tratamento de divisão por zero
* ⚠️ Tratamento de operações inválidas
* ✨ Formatação dos resultados
* 🖥️ Interface gráfica com Tkinter
* 🧪 Botão para futura calculadora científica

## 🖥️ Interface gráfica

A partir da versão **1.50.0**, o projeto passou a contar com uma interface gráfica desenvolvida utilizando Tkinter.

A interface possui:

* Visor numérico.
* Teclado numérico.
* Operadores matemáticos.
* Botão de porcentagem.
* Botão de apagar.
* Botão de limpar.
* Botão de resultado.
* Botão para futura calculadora científica.
* Cabeçalho com as opções Calculadora e Conversor.
* Menu para futuras funcionalidades.
* Tema escuro com detalhes em amarelo.
* Visor com estilo inspirado em displays digitais.

> A interface gráfica está em desenvolvimento. Algumas funcionalidades visuais ainda serão conectadas às funções da calculadora nas próximas versões.

## 📂 Estrutura do projeto

```text
calculadora-python/

├── main.py
├── calculos.py
├── historico.py
├── entradas.py
├── operacoes.py
├── apresentacao.py
├── interface.py
├── README.md
├── .gitignore
└── LICENSE
```

### 📄 Organização dos módulos

#### `main.py`

Responsável pelo fluxo principal da calculadora em terminal.

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
* `raiz()`
* `modulo()`
* `fatorial()`

#### `historico.py`

Responsável pelo gerenciamento do histórico:

* Exibição dos cálculos realizados.
* Limpeza do histórico.
* Menu de gerenciamento do histórico.
* Confirmação antes da exclusão.

#### `entradas.py`

Responsável pelo recebimento e validação das entradas informadas pelo usuário.

* Entrada de números.
* Validação das opções do menu.
* Confirmação de ações.

#### `operacoes.py`

Responsável pelo registro centralizado das operações disponíveis na calculadora.

Cada operação possui informações como:

* Nome.
* Símbolo.
* Função responsável pelo cálculo.
* Formato de apresentação.
* Quantidade de números necessários.

#### `apresentacao.py`

Responsável pela apresentação dos resultados:

* Símbolos das operações.
* Formatação dos resultados.
* Exibição dos cálculos.
* Tratamento da apresentação de números grandes e decimais.

#### `interface.py`

Responsável pela interface gráfica da calculadora utilizando Tkinter.

* Criação da janela principal.
* Criação do visor.
* Criação dos botões.
* Organização visual da calculadora.
* Aplicação do tema visual.
* Integração inicial com as operações matemáticas.

## 🛠️ Tecnologias utilizadas

* **Python**
* **Tkinter**
* **Git**
* **GitHub**
* **GitHub Desktop**
* **Visual Studio Code**

## 📚 Conceitos praticados

Durante o desenvolvimento do projeto foram aplicados conceitos importantes de programação em Python, incluindo:

* Variáveis.
* Tipos de dados.
* Operadores matemáticos.
* Condicionais.
* Loops.
* Funções.
* Listas.
* Dicionários.
* Tratamento de exceções.
* Validação de dados.
* Modularização.
* Importação de módulos.
* Organização de responsabilidades.
* Interfaces gráficas.
* Versionamento com Git.
* Semantic Versioning (SemVer).

## 📈 Evolução do projeto

O projeto foi desenvolvido de forma incremental, começando com uma calculadora simples e evoluindo conforme novos conceitos foram aprendidos.

Entre as principais evoluções estão:

**Calculadora básica → Validações → Histórico → Modularização → Novas operações → Melhorias na apresentação → Interface gráfica**

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

**1.50.0**

Principais características da versão atual:

* Operações matemáticas básicas.
* Porcentagem.
* Potência com suporte a expoentes negativos.
* Raiz quadrada.
* Módulo.
* Fatorial.
* Histórico de cálculos.
* Validação de entradas.
* Organização modular.
* Formatação dos resultados.
* Interface gráfica com Tkinter.
* Tema visual personalizado.

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

### Execute a calculadora em terminal

```bash
python main.py
```

### Execute a interface gráfica

```bash
python interface.py
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

### Raiz quadrada

```text
√25 = 5
```

### Módulo

```text
10 mod 3 = 1
```

### Fatorial

```text
5! = 120
```

## 🎯 Objetivo do projeto

O principal objetivo deste projeto é praticar programação em Python por meio do desenvolvimento incremental de uma aplicação funcional.

Além de aprender novos conceitos, o projeto também serve como exercício de:

* Organização de código.
* Separação de responsabilidades.
* Controle de versões.
* Boas práticas de desenvolvimento.
* Desenvolvimento de interfaces gráficas.
* Evolução gradual de uma aplicação.

## 👨‍💻 Autor

**Ronaldo José da Silva Junior**

Desenvolvedor de Software e Analista de Dados.

---

⭐ Projeto desenvolvido para fins de aprendizado e construção de portfólio.
