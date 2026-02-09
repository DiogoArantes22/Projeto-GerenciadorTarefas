# Projeto D – Gerenciador de Tarefas e Hábitos

Aluno: Diogo Arantes Borges Andrade  
Projeto: Projeto 1 – Semana 4 e 5  

---

## Descrição do Problema

No dia a dia, muitas pessoas têm dificuldade em organizar suas tarefas e manter hábitos importantes, como estudar regularmente ou praticar atividades físicas. A falta de organização pode causar esquecimentos e queda de produtividade.

Este projeto tem como objetivo resolver esse problema por meio de um Gerenciador de Tarefas e Hábitos, permitindo que o usuário registre suas tarefas, acompanhe se elas foram concluídas e controle a execução de hábitos ao longo do tempo.

O sistema é executado no terminal e armazena os dados em arquivos, garantindo que as informações não sejam perdidas ao fechar o programa.

---

## Principais Funcionalidades Implementadas

### Funcionalidades de Tarefas
- Cadastrar novas tarefas
- Listar todas as tarefas cadastradas
- Marcar tarefas como concluídas
- Editar tarefas
- Excluir tarefas
- Vincular tarefas a hábitos

### Funcionalidades de Hábitos
- Cadastrar novos hábitos
- Listar hábitos cadastrados
- Registrar a execução de um hábito
- Editar hábitos
- Excluir hábitos

### Relatórios
- Relatório de tarefas pendentes e concluídas
- Relatório de hábitos com a quantidade de execuções
- Exibição do progresso das tarefas vinculadas a cada hábito

---

## Como Executar o Projeto

### Pré-requisitos
- Python 3.10 ou superior instalado
- Não é necessário instalar bibliotecas externas

### Passo a passo para execução

1. Clone o repositório do projeto:
   git clone <URL_DO_REPOSITORIO>

2. Acesse a pasta do projeto:
   cd gerenciador_tarefas

3. Execute o programa principal:
   python src/main.py

4. O menu do sistema será exibido no terminal.  
   Basta escolher as opções digitando o número correspondente.

Observação:  
Os dados são salvos automaticamente na pasta `data/`, nos arquivos `tarefas.csv` e `habitos.csv`.

---

## Estrutura de Diretórios do Projeto

```
gerenciador_tarefas/
│
├── src/
│   ├── main.py                  # Arquivo principal com o menu do sistema
│   ├── models.py                # Definição das classes Tarefa e Habito
│   ├── repositorio_tarefas.py   # Manipulação do arquivo de tarefas
│   ├── repositorio_habitos.py   # Manipulação do arquivo de hábitos
│   └── relatorios.py            # Geração dos relatórios
│
├── data/
│   ├── tarefas.csv              # Arquivo de dados das tarefas
│   └── habitos.csv              # Arquivo de dados dos hábitos
│
└── README.md
```


## Considerações Finais

Este projeto foi desenvolvido com o objetivo de aplicar, na prática, os conceitos estudados no projeto LIPAI, como:

- Programação Orientada a Objetos
- Uso de classes e objetos
- Estruturas de controle (if, for, while)
- Manipulação de arquivos
- Organização de um projeto em múltiplos módulos

O código foi escrito de forma simples e organizada, facilitando a leitura, a manutenção e o entendimento do funcionamento do sistema.
