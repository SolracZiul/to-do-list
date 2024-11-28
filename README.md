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

# Estrutura Geral
O programa é dividido em funções que realizam ações específicas, como adicionar tarefas, listar, marcar como concluídas, e remover. Essas funções são chamadas dentro de um loop principal, permitindo que o usuário escolha o que deseja fazer.

# Funções
No contexto deste código, uma função é um bloco de código reutilizável que realiza uma tarefa específica. Ela ajuda a organizar o programa em partes menores e mais gerenciáveis. Cada função no código **to_do_list.py** tem um propósito claro, como exibir o menu, adicionar tarefas, ou listar tarefas.

## Exibir menu

Esta função exibe o menu principal para o usuário.

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

---

## Adicionar tarefas 

Permite que o usuário adicione uma nova tarefa à lista.

```bash
def adicionar_tarefa(lista):
    tarefa = input("Digite a nova tarefa: ")
    lista.append({"tarefa": tarefa, "concluida": False})
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")
```

- Parâmetros:
    - lista: A lista que armazena as tarefas.
- Funcionamento: 
    - Solicita ao usuário que insira o nome da tarefa.
    - Adiciona a tarefa à lista, como um dicionário contendo:
        1. A descrição da tarefa ("tarefa").
        2. O status de conclusão ("concluida": False).
    - Exibe uma mensagem de confirmação.

---

## Listar tarefas

Exibe todas as tarefas da lista, indicando se estão concluídas.

```bash
def listar_tarefas(lista):
    if not lista:
        print("Nenhuma tarefa encontrada.")
        return
    print("\nTarefas:")
    for i, item in enumerate(lista):
        status = "[✔]" if item["concluida"] else "[ ]"
        print(f"{i + 1}. {status} {item['tarefa']}")
```

- Parâmetros:
    - lista: A lista de tarefas.
- Funcionamento:
    - Verifica se a lista está vazia. Caso esteja, informa ao usuário.
    - Caso contrário, exibe todas as tarefas com um índice numérico.
    - Mostra o status:
        1. [✔]: Tarefa concluída.
        2. [🔄]: Tarefa pendente.

---

## Marcar concluída 

Permite que o usuário marque uma tarefa como concluída.

```bash
def marcar_concluida(lista):
    listar_tarefas(lista)
    try:
        indice = int(input("Digite o número da tarefa para marcar como concluída: ")) - 1
        if 0 <= indice < len(lista):
            lista[indice]["concluida"] = True
            print(f"Tarefa '{lista[indice]['tarefa']}' marcada como concluída!")
        else:
            print("Número inválido!")
    except ValueError:
        print("Entrada inválida! Digite um número.")
```

- Parâmetros:
    - lista: A lista de tarefas.
- Funcionamento:
    - Exibe as tarefas com listar_tarefas.
    - Solicita o número da tarefa a ser marcada como concluída.
    - Valida o número informado:
        1. Se válido, altera "concluida" para True.
        2. Caso contrário, exibe uma mensagem de erro.

---

## Remover tarefa 

Remove uma tarefa da lista.

```bash
def remover_tarefa(lista):
    listar_tarefas(lista)
    try:
        indice = int(input("Digite o número da tarefa para remover: ")) - 1
        if 0 <= indice < len(lista):
            tarefa = lista.pop(indice)
            print(f"Tarefa '{tarefa['tarefa']}' removida com sucesso!")
        else:
            print("Número inválido!")
    except ValueError:
        print("Entrada inválida! Digite um número.")
```

- Parâmetros:
    - lista: A lista de tarefas.
- Funcionamento:
    - Exibe as tarefas com listar_tarefas.
    - Solicita o número da tarefa a ser removida.
    - Valida o número e remove a tarefa correspondente da lista.

---

## Função Principal

O coração do programa, que controla o fluxo de execução.

```bash
def main():
    tarefas = []
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            adicionar_tarefa(tarefas)
        elif escolha == "2":
            listar_tarefas(tarefas)
        elif escolha == "3":
            marcar_concluida(tarefas)
        elif escolha == "4":
            remover_tarefa(tarefas)
        elif escolha == "5":
            print("Saindo... Até mais!")
            break
        else:
            print("Opção inválida! Tente novamente.")
```

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
