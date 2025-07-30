tarefas = []

while True:
    print("\n--- To-Do List ---")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Marcar como concluída")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tarefa = input("Digite a tarefa: ")
        tarefas.append({"tarefa": tarefa, "concluida": False})
        print("Tarefa adicionada!")
    
    elif opcao == "2":
        print("\n--- Tarefas ---")
        for i, tarefa in enumerate(tarefas):
            status = "✓" if tarefa["concluida"] else " "
            print(f"{i+1}. [{status}] {tarefa['tarefa']}")
    
    elif opcao == "3":
        num = int(input("Número da tarefa concluída: ")) - 1
        if 0 <= num < len(tarefas):
            tarefas[num]["concluida"] = True
            print("Tarefa marcada!")
        else:
            print("Número inválido!")
    
    elif opcao == "4":
        break

print("Até logo!")