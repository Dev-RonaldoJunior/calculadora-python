# 🧮 Calculadora Básica em Python

Projeto desenvolvido para praticar conceitos de programação em Python, como lógica de programação, estruturas de repetição, condicionais, tratamento de erros, listas, funções e modularização.

## 📌 Sobre o projeto

Uma calculadora executada pelo terminal, desenvolvida de forma incremental durante meus estudos de Python e utilizada como parte do meu portfólio.

O projeto evolui por meio de versões, permitindo acompanhar a implementação de novas funcionalidades, refatorações, correções e melhorias na organização do código.

Atualmente, o projeto utiliza o padrão **Semantic Versioning (SemVer)** para identificar suas versões:

```text
MAJOR.MINOR.PATCH
│     │     │
│     │     └── Correções pequenas e bugs
│     └──────── Novas funcionalidades compatíveis
└────────────── Mudanças grandes ou incompatíveis
```

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
* Apresentação dos resultados organizada em módulo próprio

## 📂 Estrutura do projeto

```text
calculadora/
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

Responsável pelo fluxo principal da calculadora, execução do programa, controle do menu, processamento das operações e integração entre os demais módulos.

### `calculos.py`

Contém as funções responsáveis pelas operações matemáticas:

* `somar()`
* `subtrair()`
* `multiplicar()`
* `dividir()`

### `historico.py`

Responsável pelas funcionalidades relacionadas ao histórico de cálculos:

* `mostrar_historico()`
* `limpar_historico()`
* `menu_historico()`

### `entradas.py`

Responsável pela entrada e validação dos números informados pelo usuário:

* `input_numero1()`
* `input_numero2()`

### `validacoes.py`

Responsável pelas validações das operações matemáticas:

* `validar_operacao()`

### `apresentacao.py`

Responsável pela apresentação dos resultados e pelos símbolos das operações:

* `simbolo_operacao()`
* `mostrar_resultado()`
* `SIMBOLOS_OPERACOES`

## 🛠️ Tecnologias utilizadas

* Python
* Visual Studio Code
* Git
* GitHub
* GitHub Desktop

## 📋 Histórico de versões

### 1.0.0 — Versão inicial

* Soma
* Subtração
* Multiplicação
* Divisão
* Menu de operações
* Encerramento da calculadora

### 1.1.0 — Validação inicial

* Tratamento de valores inválidos
* Tratamento de divisão por zero

### 1.2.0 — Histórico de cálculos

* Criação do histórico de cálculos

### 1.3.0 — Visualização do histórico

* Visualização do histórico
* Mensagem para histórico vazio

### 1.4.0 — Limpeza do histórico

* Limpeza do histórico
* Criação do submenu de histórico

### 1.5.0 — Confirmação de limpeza

* Confirmação antes de limpar o histórico
* Opções de confirmação ou cancelamento

### 1.6.0 — Módulo de cálculos

* Operações matemáticas separadas no arquivo `calculos.py`
* Criação das funções de soma, subtração, multiplicação e divisão
* Importação do módulo `calculos`
* Separação do projeto em arquivos

### 1.7.0 — Organização do menu

* Criação da função `mostrar_menu()`
* Organização do menu em uma função própria
* Melhoria na organização do código

### 1.8.0 — Organização do histórico

* Criação das funções `mostrar_historico()` e `limpar_historico()`
* Organização das funções relacionadas ao histórico
* Histórico passado como parâmetro

### 1.9.0 — Organização das entradas

* Criação da função `input_numero()`
* Separação da entrada dos números
* Retorno dos números através da função
* Tratamento de valores inválidos

### 1.10.0 — Organização do cálculo

* Criação da função `realizar_calculo()`
* Criação da função `simbolo_operacao()`
* Validação da operação antes da entrada dos números
* Tratamento de divisão por zero
* Melhor organização do fluxo principal
* Formatação do histórico de cálculos
* Correção do nome `imput_numero()` para `input_numero()`

### 1.11.0 — Função principal

* Criação da função `main()`
* Movimentação do histórico para dentro da função principal
* Movimentação do `while` para dentro da função principal
* Implementação de `if __name__ == "__main__":`
* Melhor organização da execução do programa
* Preparação do código para futuros testes automatizados

### 1.12.0 — Submenu de histórico

* Criação da função `menu_historico()`
* Separação do submenu de histórico da função `main()`
* Organização das opções do histórico
* Histórico passado como parâmetro
* Melhoria no fluxo principal

### 1.13.0 — Validação das operações

* Criação da função `validar_operacao()`
* Validação das operações matemáticas
* Validação das opções de 1 a 4
* Separação da validação da função `main()`
* Melhoria na organização do código

### 1.14.0 — Separação das entradas

* Separação da entrada do primeiro e segundo número
* Criação da função `input_numero1()`
* Criação da função `input_numero2()`
* Validação independente dos dois números
* Melhoria no tratamento de valores inválidos
* Organização da entrada de dados em funções específicas

### 1.15.0 — Repetição das entradas inválidas

* Implementação de repetição da entrada de números inválidos
* Utilização de `while` nas funções `input_numero1()` e `input_numero2()`
* Tratamento de erros através de `try/except`
* O programa continua solicitando o número até que um valor válido seja informado
* Remoção da necessidade de retornar `None` em caso de erro
* Melhoria no fluxo de entrada dos números

### 1.16.0 — Repetição do submenu

* Implementada repetição do submenu de histórico utilizando `while`
* Validação contínua das opções do submenu
* Utilização de `break` após uma opção válida
* Opção 1 chama `mostrar_historico()`
* Opção 2 chama `limpar_historico()`
* Opções inválidas não encerram mais o submenu
* Melhorado o fluxo de navegação do menu de histórico

### 1.17.0 — Repetição da confirmação

* Implementada repetição da confirmação para limpar o histórico
* Adicionado `while True` na função `limpar_historico()`
* Respostas `S` e `N` encerram a confirmação com `break`
* Respostas inválidas continuam solicitando uma nova opção
* Melhorado o fluxo de limpeza do histórico

### 1.18.0 — Apresentação dos resultados

* Criada a função `mostrar_resultado()`
* Melhorada a apresentação dos resultados
* Exibição da operação completa com seus respectivos números
* Reutilização da função `simbolo_operacao()`
* Organização da exibição do resultado dentro de uma função própria

### 1.19.0 — Centralização das operações válidas

* Criada a constante `OPERACOES_VALIDAS`
* Centralizada a definição das operações matemáticas disponíveis
* Atualizada a função `validar_operacao()` para utilizar a constante
* Melhorada a organização e manutenção do código
* Reduzida a repetição das opções válidas no processo de validação

### 1.20.0 — Centralização dos símbolos

* Criada a constante `SIMBOLOS_OPERACOES`
* Centralizados os símbolos das operações em um dicionário
* Atualizada a função `simbolo_operacao()` para utilizar o dicionário
* Removidos os `if/elif` da função `simbolo_operacao()`
* Melhorada a organização e manutenção dos símbolos das operações
* Mantido o uso dos símbolos no resultado e no histórico

### 1.21.0 — Centralização das funções de cálculo

* Criada a constante `OPERACOES_CALCULO`
* Centralizadas as funções de cálculo em um dicionário
* Atualizada a função `realizar_calculo()` para utilizar o dicionário
* Removidos os `if/elif` da função `realizar_calculo()`
* Melhorada a organização e manutenção das operações matemáticas
* Mantida a integração com o módulo `calculos.py`

### 1.22.0 — Módulo de histórico

* Criado o módulo `historico.py`
* Movidas as funções de histórico para um módulo separado
* Criada a função `mostrar_historico()` no módulo de histórico
* Criada a função `limpar_historico()` no módulo de histórico
* Criada a função `menu_historico()` no módulo de histórico
* Atualizado o `main.py` para importar e utilizar o módulo `historico`
* Melhorada a organização e separação de responsabilidades do projeto
* Mantido o histórico de cálculos funcionando por meio de uma lista compartilhada entre as funções

### 1.23.0 — Módulo de entradas

* Criado o módulo `entradas.py`
* Movidas as funções `input_numero1()` e `input_numero2()` para um módulo separado
* Atualizado o `main.py` para importar e utilizar o módulo `entradas`
* Melhorada a organização e separação de responsabilidades do projeto
* Mantido o tratamento de valores inválidos nas funções de entrada
* Mantido o fluxo principal da calculadora funcionando normalmente

### 1.24.0 — Módulo de validações

* Criado o módulo `validacoes.py`
* Movida a função `validar_operacao()` para um módulo separado
* Atualizado o `main.py` para importar e utilizar o módulo `validacoes`
* A lista `OPERACOES_VALIDAS` passou a ser enviada como parâmetro para a função de validação
* Melhorada a organização e separação de responsabilidades do projeto
* Mantida a validação das operações matemáticas disponíveis

### 1.25.0 — Modularização do menu

* Criado o módulo `menu.py`
* Movida a função `mostrar_menu()` para um módulo separado
* Atualizado o `main.py` para importar e utilizar o módulo `menu`

> Esta alteração foi posteriormente revertida após uma revisão arquitetural, pois a criação de um módulo exclusivo para uma única função não trouxe benefícios suficientes para o tamanho atual do projeto.

### 1.26.0 — Módulo de apresentação

* Criado o módulo `apresentacao.py`
* Movidas as funções `simbolo_operacao()` e `mostrar_resultado()` para um módulo separado
* Movida a constante `SIMBOLOS_OPERACOES` para o módulo `apresentacao`
* Atualizado o `main.py` para importar e utilizar o módulo `apresentacao`
* Centralizada a apresentação dos resultados e símbolos das operações

### 1.26.1 — Correção arquitetural

* Removido o módulo `menu.py`
* Restaurada a função `mostrar_menu()` no `main.py`
* Removida a importação do módulo `menu`
* Ajustado o fluxo de exibição do menu principal
* Revisada a arquitetura do projeto para evitar modularização excessiva
* Mantidos os demais módulos da aplicação
* Mantida a funcionalidade do menu principal
* Reavaliada a organização dos módulos considerando a responsabilidade e o tamanho atual do projeto

## 🔮 Próximas versões

As próximas versões serão definidas considerando a evolução técnica do projeto e evitando alterações estruturais que adicionem complexidade sem benefícios claros.

Possíveis melhorias:

* Revisar e melhorar a organização da função `main()`
* Adicionar novas operações matemáticas
* Permitir cálculos com mais de dois números
* Melhorar o sistema de histórico
* Implementar persistência do histórico
* Permitir exportação do histórico
* Implementar testes automatizados
* Melhorar o tratamento de exceções
* Criar uma interface gráfica
* Realizar uma refatoração geral conforme a complexidade do projeto aumentar

As versões futuras seguirão o padrão **Semantic Versioning (SemVer)**:

* **PATCH (`1.26.2`)** — correções pequenas e ajustes
* **MINOR (`1.27.0`)** — novas funcionalidades compatíveis
* **MAJOR (`2.0.0`)** — mudanças grandes ou incompatíveis

## ▶️ Como executar

Certifique-se de ter o Python instalado e execute:

```bash
python main.py
```

## 👨‍💻 Autor

**Ronaldo José da Silva Junior**

Projeto desenvolvido para estudos de Python e construção de portfólio.
