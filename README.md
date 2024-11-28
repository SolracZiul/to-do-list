# Planejamento to-do-list

# Objetivo
- Contruir um programa em Python que permita:
    1. Adicionar tarefas
    2. Listar tarefas pendentes
    3. Marcar tarefas como concluídas
    4. Remover tarefas

# Estrutura do projeto
-  O programa será baseado no terminal, com um menu simples que permite interagir com as tarefas.

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
- exibir_menu()
    - Esta função exibe o menu principal para o usuário.
    1. Objetivo: Mostrar as opções disponíveis para o usuário.
    2. Uso: É chamada no início de cada ciclo do programa.

-  adicionar_tarefa(lista)
    Permite que o usuário adicione uma nova tarefa à lista.

    -  Parâmetros:
        lista: A lista que armazena as tarefas.
    - Funcionamento: 
        1. Solicita ao usuário que insira o nome da tarefa.
        2. Adiciona a tarefa à lista, como um dicionário contendo:
            - A descrição da tarefa ("tarefa").
            - O status de conclusão ("concluida": False).
        3. Exibe uma mensagem de confirmação.
    
    - listar_tarefas(lista)
    Exibe todas as tarefas da lista, indicando se estão concluídas.

    - Parâmetros:
        lista: A lista de tarefas.
    - Funcionamento:
        1. Verifica se a lista está vazia. Caso esteja, informa ao usuário.
        2. Caso contrário, exibe todas as tarefas com um índice numérico.
        3. Mostra o status:
            - [✔]: Tarefa concluída.
            - [ ]: Tarefa pendente.

    - marcar_concluida(lista)
    Permite que o usuário marque uma tarefa como concluída.

    - Parâmetros:
        lista: A lista de tarefas.
    - Funcionamento:
        1. Exibe as tarefas com listar_tarefas.
        2. Solicita o número da tarefa a ser marcada como concluída.
        3. Valida o número informado:
            - Se válido, altera "concluida" para True.
            - Caso contrário, exibe uma mensagem de erro.

    - remover_tarefa(lista)
    Remove uma tarefa da lista.

    - Parâmetros:
        lista: A lista de tarefas.
    - Funcionamento:
        1. Exibe as tarefas com listar_tarefas.
        2. Solicita o número da tarefa a ser removida.
        3. Valida o número e remove a tarefa correspondente da lista.

    - Função Principal (main)
        O coração do programa, que controla o fluxo de execução.
        
    - Objetivo: Gerenciar as interações do usuário com base no menu.
    - Funcionamento:
        1. Inicializa uma lista vazia tarefas para armazenar as tarefas.
        2. Exibe o menu e solicita a escolha do usuário.
        3. Executa a ação correspondente, chamando as funções apropriadas.
        4. Sai do programa se o usuário escolher a opção "5".

# Resumo
O programa usa listas e dicionários para gerenciar tarefas, além de funções separadas para modularidade. O fluxo é simples:

1. Adicionar tarefas.
2. Listar para verificar o progresso.
3. Marcar como concluída quando finalizadas.
4. Remover tarefas desnecessárias.
