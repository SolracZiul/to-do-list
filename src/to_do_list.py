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

teste