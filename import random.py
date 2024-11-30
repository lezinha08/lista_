def exibir_tarefas(tarefas):
    if len(tarefas) == 0:
        print("\nA lista de tarefas está vazia.")
    else:
        print("\nLista de Tarefas:")
        for i, tarefa in enumerate(tarefas, 1):
            print(f"{i}. {tarefa}")

def adicionar_tarefa(tarefas):
    nova_tarefa = input("\nDigite a tarefa que deseja adicionar: ")
    tarefas.append(nova_tarefa)
    print(f"Tarefa '{nova_tarefa}' adicionada com sucesso!")

def remover_tarefa(tarefas):
    exibir_tarefas(tarefas)
    if len(tarefas) > 0:
        try:
            indice = int(input("\nDigite o número da tarefa que deseja remover: "))
            if 1 <= indice <= len(tarefas):
                tarefa_removida = tarefas.pop(indice - 1)
                print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
            else:
                print("Número inválido.")
        except ValueError:
            print("Por favor, digite um número válido.")

def menu():
    print("\nEscolha uma opção:")
    print("1. Exibir tarefas")
    print("2. Adicionar tarefa")
    print("3. Remover tarefa")
    print("4. Sair")

def lista_tarefas():
    print("Bem-vindo ao Gerenciador de Lista de Tarefas!")
    tarefas = []

    while True:
        menu()
        opcao = input("\nDigite a opção desejada: ")

        if opcao == '1':
            exibir_tarefas(tarefas)
        elif opcao == '2':
            adicionar_tarefa(tarefas)
        elif opcao == '3':
            remover_tarefa(tarefas)
        elif opcao == '4':
            print("\nSaindo do programa. Até mais!")
            break
        else:
            print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    lista_tarefas()
