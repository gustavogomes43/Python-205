'''2 - Crie um programa que  acesse a API Random User Generator para buscar um usuário fictício aleatório. exibindo o nome, e-mail e país desse usuário, caso houver erro na conexão, mostre uma mensagem de falha.'''

import urllib.request
import json

print("=== USUÁRIO ALEATÓRIO ===")

try:
    # Acessa o site da API que gera usuários aleatórios
    resposta = urllib.request.urlopen("https://randomuser.me/api/")

    # Lê a resposta e converte de texto para um formato que o Python entende (JSON)
    dados = json.loads(resposta.read().decode())

    # Pega o primeiro usuário da lista de resultados
    usuario = dados["results"][0]

    # Pega as informações que queremos: nome, e-mail e país
    nome = usuario["name"]["first"] + " " + usuario["name"]["last"]
    email = usuario["email"]
    pais = usuario["location"]["country"]

    # Mostra na tela
    print("\nNome:", nome)
    print("E-mail:", email)
    print("País:", pais)

except:
    # Se der erro (sem internet ou outro problema)
    print("Não foi possível acessar a API. Verifique sua conexão.")