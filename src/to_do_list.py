def exibir_menu():
    print("\n--- To-Do List ---")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Marcar Tarefa como Concluída")
    print("4. Remover Tarefa")
    print("5. Sair")

def adicionar_tarefa(lista):
    tarefa = input("Digite a nova tarefa: ")
    lista.append({"tarefa": tarefa, "concluida": False})
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")

def listar_tarefas(lista):
    if not lista:
        print("Nenhuma tarefa encontrada.")
        return
    print("\nTarefas:")
    for i, item in enumerate(lista):
        status = "[✔]" if item["concluida"] else "[ ]"
        print(f"{i + 1}. {status} {item['tarefa']}")