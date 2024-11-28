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

if __name__ == "__main__":
    main()
