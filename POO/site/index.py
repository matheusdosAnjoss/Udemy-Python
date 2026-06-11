import requests

# O link (URL) do servidor que queremos consultar
url = "https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/35817500#content"

# O HTTP entra em ação fazendo o "pedido" (GET)
resposta = requests.get(url)

# Verificando se o servidor respondeu com sucesso (Código 200 significa "Ok")
if resposta.status_code == 200:
    # Transformando a resposta em um dicionário Python (JSON)
    # dados = resposta.json()
    print(resposta)
    print('Funcionou!')
    # print(f"Logradouro: {dados['logradouro']}")
    # print(f"Bairro: {dados['bairro']}")
    # print(f"Cidade: {dados['localidade']}/{dados['uf']}")
else:
    print(f"Erro ao acessar o servidor: {resposta.status_code}")