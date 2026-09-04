# 🧮 Calculadora Básica em Python

Projeto desenvolvido em Python com o objetivo de praticar lógica de programação, organização de código, modularização e evolução incremental de um projeto utilizando Git e GitHub.

## 📌 Sobre o projeto

A **Calculadora Básica em Python** começou como uma aplicação simples executada pelo terminal e foi evoluindo gradualmente, recebendo novas funcionalidades e melhorias de organização.

O projeto utiliza módulos separados por responsabilidade, mantendo uma estrutura simples e evitando uma modularização excessiva.

Atualmente, a calculadora possui operações matemáticas, sistema de histórico e validação de entradas.

## 🚀 Funcionalidades

* ➕ Soma
* ➖ Subtração
* ✖️ Multiplicação
* ➗ Divisão
* 📊 Porcentagem
* 🔢 Potência
* 📜 Visualização do histórico
* 🗑️ Limpeza do histórico
* ⚠️ Validação de operações
* ⚠️ Tratamento de entradas numéricas inválidas
* ⚠️ Tratamento de divisão por zero
* 🔄 Repetição de menus e entradas inválidas
* 💻 Execução pelo terminal

## 📁 Estrutura do projeto

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

## 🧩 Organização dos módulos

### `main.py`

Responsável pelo fluxo principal da aplicação:

* Exibição do menu principal
* Controle da execução da calculadora
* Validação da operação escolhida
* Recebimento dos números
* Execução dos cálculos
* Armazenamento dos resultados no histórico

### `calculos.py`

Contém as funções responsáveis pelas operações matemáticas:

* `somar()`
* `subtrair()`
* `multiplicar()`
* `dividir()`
* `porcentagem()`
* `potencia()`

### `historico.py`

Responsável pelo gerenciamento do histórico:

* Visualização dos cálculos realizados
* Limpeza do histórico
* Menu do histórico
* Confirmação antes da exclusão

### `entradas.py`

Responsável pelo recebimento e validação dos números informados pelo usuário.

### `validacoes.py`

Responsável pela validação das operações disponíveis na calculadora.

### `apresentacao.py`

Responsável pela apresentação dos resultados e símbolos das operações.

## 🛠️ Tecnologias utilizadas

* **Python**
* **Git**
* **GitHub**
* **GitHub Desktop**
* **Visual Studio Code**

## 📦 Versionamento

O projeto utiliza **Semantic Versioning (SemVer)**:

```text
MAJOR.MINOR.PATCH
```

* **MAJOR:** alterações grandes ou incompatíveis.
* **MINOR:** novas funcionalidades compatíveis com a versão anterior.
* **PATCH:** correções de bugs e pequenas correções.

## 📚 Histórico de versões

### 1.0.0

* Criada a calculadora básica.
* Implementadas as operações de soma, subtração, multiplicação e divisão.
* Criado menu principal.
* Adicionada opção para encerrar a aplicação.

### 1.1.0

* Adicionado tratamento para entradas inválidas.
* Adicionado tratamento de divisão por zero.

### 1.2.0

* Criado sistema inicial de histórico de cálculos.

### 1.3.0

* Adicionada visualização do histórico.
* Adicionada mensagem para histórico vazio.

### 1.4.0

* Adicionada opção para limpar o histórico.
* Criado submenu de histórico.

### 1.5.0

* Adicionada confirmação antes da limpeza do histórico.
* Implementadas opções de confirmação e cancelamento.

### 1.6.0

* Criado o módulo `calculos.py`.
* Operações matemáticas separadas em funções.
* Implementado sistema de importação das funções.

### 1.7.0

* Criada a função `mostrar_menu()`.

### 1.8.0

* Criada a função `mostrar_historico()`.
* Criada a função `limpar_historico()`.
* Histórico passou a ser recebido como parâmetro.

### 1.9.0

* Criada a função `input_numero()` para entrada dos números.

### 1.10.0

* Criada a função `realizar_calculo()`.
* Criada a função `simbolo_operacao()`.
* Implementada validação da operação antes da entrada dos números.
* Melhorado o tratamento da divisão por zero.
* Melhorada a formatação do histórico.
* Corrigido o nome da função `imput_numero()` para `input_numero()`.

### 1.11.0

* Criada a função `main()`.
* Transferido o fluxo principal da aplicação para `main()`.
* Adicionado `if __name__ == "__main__":`.
* Estrutura preparada para futuros testes.

### 1.12.0

* Criada a função `menu_historico()`.

### 1.13.0

* Criada a função `validar_operacao()`.

### 1.14.0

* Criadas as funções `input_numero1()` e `input_numero2()`.

### 1.15.0

* Implementada repetição da entrada de números inválidos.
* Melhorado o tratamento de exceções nas entradas numéricas.

### 1.16.0

* Implementada repetição do submenu de histórico em caso de opção inválida.

### 1.17.0

* Implementada repetição da confirmação de limpeza do histórico em caso de opção inválida.

### 1.18.0

* Criada a função `mostrar_resultado()`.

### 1.19.0

* Criada a constante `OPERACOES_VALIDAS`.

### 1.20.0

* Criado o dicionário `SIMBOLOS_OPERACOES`.

### 1.21.0

* Criado o dicionário `OPERACOES_CALCULO`.
* Centralizado o relacionamento entre opções e funções matemáticas.

### 1.22.0

* Criado o módulo `historico.py`.
* Movidas as funções relacionadas ao histórico para o novo módulo.

### 1.23.0

* Criado o módulo `entradas.py`.
* Movidas as funções de entrada de números para o novo módulo.

### 1.24.0

* Criado o módulo `validacoes.py`.
* Movida a função `validar_operacao()` para o novo módulo.
* `OPERACOES_VALIDAS` passou a ser recebida como parâmetro.

### 1.25.0

* Avaliada a separação das responsabilidades relacionadas ao menu.
* A criação do módulo `menu.py` foi posteriormente revertida para evitar modularização excessiva.

### 1.26.0

* Criado o módulo `apresentacao.py`.
* Movidas as funções relacionadas à apresentação dos resultados.
* Movida a constante `SIMBOLOS_OPERACOES`.

### 1.26.1

* Corrigida a arquitetura após revisão.
* Removido o módulo `menu.py`.
* Restaurada a função `mostrar_menu()` no `main.py`.
* Removido import desnecessário relacionado ao módulo excluído.
* Mantida a separação de responsabilidades sem excesso de modularização.

### 1.27.0

* Adicionada a operação de porcentagem.
* Criada a função `porcentagem()` em `calculos.py`.
* Adicionada a porcentagem ao menu principal.
* Integrada a nova operação ao dicionário `OPERACOES_CALCULO`.
* Adicionado o símbolo `%` em `apresentacao.py`.
* Criada a função `formatar_resultado()`.
* Implementada formatação específica para cálculos de porcentagem.
* Resultados formatados passaram a ser armazenados no histórico.

### 1.28.0

* Adicionada a operação de potência.
* Criada a função `potencia()` em `calculos.py`.
* Adicionada a potência ao menu principal.
* Integrada a nova operação ao dicionário `OPERACOES_CALCULO`.
* Adicionado o símbolo `^` em `apresentacao.py`.
* Ajustada a opção do histórico para a posição 7.
* Implementada a potência utilizando repetição com `while`.
* Mantido o armazenamento dos cálculos de potência no histórico.

## 🔮 Próximas versões

O projeto continuará evoluindo gradualmente, priorizando aprendizado, organização e boas práticas de desenvolvimento.

Possíveis evoluções:

* Melhorias nas operações matemáticas
* Expansão do sistema de histórico
* Persistência dos cálculos
* Exportação do histórico
* Melhor tratamento de exceções
* Implementação de testes automatizados
* Interface gráfica
* Novos recursos para a calculadora

## ▶️ Como executar

Certifique-se de ter o Python instalado.

Clone o repositório:

```bash
git clone https://github.com/Dev-RonaldoJunior/calculadora-python.git
```

Entre na pasta:

```bash
cd calculadora-python
```

Execute:

```bash
python main.py
```

## 👨‍💻 Autor

**Ronaldo José da Silva Junior**

Projeto desenvolvido para estudos e construção de portfólio em Python.
