import json

def LerInt(msg):
    while True: # ALTERADO: Adicionado loop para não retornar vazio
        try:
            n = int(input(msg))
            return n
        except(ValueError, TypeError):
            print('[ERRO]: Digite um numero válido!')
        
def titulo(msg):
    print('=='*15)
    print(msg.center(30))
    print('=='*15)

def linha(tam=12):
    print('=='*tam)

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
    if not tarefasRefazer:
        print('Nada para refazer.')
        return
    
    tarefa = tarefasRefazer.pop()
    tarefas.append(tarefa)
    titulo(f'Tarefa "{tarefa}" refeita com sucesso!')

def ler_tarefas(caminho_arquivo):
    """Tenta carregar as tarefas do arquivo JSON. Se não existir, retorna lista vazia."""
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print('Arquivo não existir!')
        return [] # Primeira vez rodando o programa, o arquivo ainda não existe

def SalvarTarefas(tarefas):
    with open("list_tarefa.json", 'w', encoding='utf8') as arquivo:
        json.dump(
            tarefas,
            arquivo,
            indent=4,
            ensure_ascii=False
        )
    
CAMINHO_ARQUIVO = 'list_tarefa.json'
tarefas = ler_tarefas(CAMINHO_ARQUIVO)
tarefa_refazer = []

while True:         #aula 195 10:20
    titulo('LISTA DE TAREFAS')
    
    print("\n1 - Adicionar tarefa")
    print("2 - Desfazer")
    print("3 - Refazer")
    print("4 - Mostrar tarefas")
    print("0 - Sair")

    opcao = LerInt('Escolha: ')
    linha()
    if opcao == 1:
        tarefa = str(input('Digite a tarefa: '))
        tarefas.append(tarefa)
        linha()
        print('TAREFAS:')
        mostraTarefa(tarefas)
        SalvarTarefas(tarefas)

    elif opcao == 2:
        desfazer(tarefas, tarefa_refazer)
        SalvarTarefas(tarefas)
        mostraTarefa(tarefas)

    elif opcao == 3:
        refazer(tarefas, tarefa_refazer)
        SalvarTarefas(tarefas)
        mostraTarefa(tarefas)

    elif opcao == 4:
        mostraTarefa(tarefas)

    elif opcao == 0:
        break

