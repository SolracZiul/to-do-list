<div align="center">
# Planejamento to-do-list
</div>

# Objetivo
Contruir um programa em Python que permita:
- Adicionar tarefas
- Listar tarefas pendentes
- Marcar tarefas como concluídas
- Remover tarefas

# Estrutura do projeto
O programa será baseado no terminal, com um menu simples que permite interagir com as tarefas.

# Cronograma
- Dia 1: Configurar o ambiente e estruturar o projeto.
- Dia 2: Implementar as funcionalidades 'Adicionar tarefas' e 'Listar tarefas pendentes'.
- Dia 3: Implementar as funcionalidades 'Marcar tarefas como concluídas' e 'Remover tarefas'.
- Dia 4: Analise de possíveis melhorias e implementação de novas funcionalidades. 
- Dia 5: Testes e ajustes finais.

# Funcionamento do programa

O código to_do_list.py implementa um to-do list em Python no formato de terminal, com funcionalidades básicas de gerenciamento de tarefas. Vamos explicar parte por parte.

1. Estrutura Geral
- O programa é dividido em funções que realizam ações específicas, como adicionar tarefas, listar, marcar como concluídas, e remover. Essas funções são chamadas dentro de um loop principal, permitindo que o usuário escolha o que deseja fazer.

2. Funções
- exibir_menu(): Esta função exibe o menu principal para o usuário.

```bash
def exibir_menu():
    print("\n--- To-Do List ---")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Marcar Tarefa como Concluída")
    print("4. Remover Tarefa")
    print("5. Sair")
```

- Objetivo: Mostrar as opções disponíveis para o usuário.
- Uso: É chamada no início de cada ciclo do programa.

- adicionar_tarefa(lista): Permite que o usuário adicione uma nova tarefa à lista.

    - Parâmetros:
        - lista: A lista que armazena as tarefas.
    - Funcionamento: 
        - Solicita ao usuário que insira o nome da tarefa.
        - Adiciona a tarefa à lista, como um dicionário contendo:
            1. A descrição da tarefa ("tarefa").
            2. O status de conclusão ("concluida": False).
        - Exibe uma mensagem de confirmação.
    
- listar_tarefas(lista): Exibe todas as tarefas da lista, indicando se estão concluídas.
    - Parâmetros:
        - lista: A lista de tarefas.
    - Funcionamento:
        - Verifica se a lista está vazia. Caso esteja, informa ao usuário.
        - Caso contrário, exibe todas as tarefas com um índice numérico.
        - Mostra o status:
            1. [✔]: Tarefa concluída.
            2. [  ]: Tarefa pendente.

- marcar_concluida(lista): Permite que o usuário marque uma tarefa como concluída.
    - Parâmetros:
        - lista: A lista de tarefas.
    - Funcionamento:
        - Exibe as tarefas com listar_tarefas.
        - Solicita o número da tarefa a ser marcada como concluída.
        - Valida o número informado:
            1. Se válido, altera "concluida" para True.
            2. Caso contrário, exibe uma mensagem de erro.

- remover_tarefa(lista): Remove uma tarefa da lista.
    - Parâmetros:
        - lista: A lista de tarefas.
    - Funcionamento:
        - Exibe as tarefas com listar_tarefas.
        - Solicita o número da tarefa a ser removida.
        - Valida o número e remove a tarefa correspondente da lista.

- Função Principal (main): O coração do programa, que controla o fluxo de execução.
    - Objetivo: Gerenciar as interações do usuário com base no menu.
    - Funcionamento:
        - Inicializa uma lista vazia tarefas para armazenar as tarefas.
        - Exibe o menu e solicita a escolha do usuário.
        - Executa a ação correspondente, chamando as funções apropriadas.
        - Sai do programa se o usuário escolher a opção "5".

# Resumo
O programa usa listas e dicionários para gerenciar tarefas, além de funções separadas para modularidade. O fluxo é simples:

1. Adicionar tarefas.
2. Listar para verificar o progresso.
3. Marcar como concluída quando finalizadas.
4. Remover tarefas desnecessárias.
