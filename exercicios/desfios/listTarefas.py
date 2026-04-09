def mostraTarefa(tarefas):
    if not tarefas:
        print("Listar Vazia")
        return

    for i, tarefa in enumerate(tarefas):
        print(f'{i+1} - {tarefa}')


def desfazer(tarefas, tarefasRefazer):
    if not tarefas:
        print('Nada para desfazer.')
        return 
    
    tarefa = tarefas.pop()
    tarefasRefazer.append(tarefa)
    

def refazer(tarefas, tarefasRefazer):
    if not tarefas:
        print('Nada para refazer.')
        return
    
    tarefa = tarefasRefazer.pop()
    tarefas.append(tarefa)
    

tarefas = []
tarefa_refazer = []

while True:         #aula 195 10:20
    print("\n1 - Adicionar tarefa")
    print("2 - Desfazer")
    print("3 - Refazer")
    print("4 - Mostrar tarefas")
    print("0 - Sair")

    opcao = int(input('Escolha: '))
    

    if opcao == 1:
        tarefa = str(input('Digite a tarefa: '))
        tarefas.append(tarefa)
        print('TAREFAS:')
        mostraTarefa(tarefas)

    elif opcao == 2:
        desfazer(tarefas, tarefa_refazer)
        mostraTarefa(tarefas)

    elif opcao == 3:
        refazer(tarefas, tarefa_refazer)
        mostraTarefa(tarefas)

    elif opcao == 4:
        mostraTarefa(tarefas)

    elif opcao == 0:
        break

