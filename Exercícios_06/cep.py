'''3 - Crie um programa que consulte informações de um CEP na API ViaCEP, retorne logradouro, bairro, cidade e estado do CEP digitado, caso o CEP não existir ou houver erro na requisição, mostre uma mensagem de falha.'''

import urllib.request
import json

print("=== CONSULTA DE CEP ===")

# Pede o CEP para o usuário
cep = input("Digite o CEP (somente números): ")

# Monta o endereço da API com o CEP informado
url = f"https://viacep.com.br/ws/{cep}/json/"

try:
    # Faz a requisição (acessa a API)
    resposta = urllib.request.urlopen(url)
    dados = json.loads(resposta.read().decode())

    # Verifica se o CEP existe
    if "erro" in dados:
        print("CEP não encontrado.")
    else:
        # Mostra as informações do endereço
        print("\nLogradouro:", dados["logradouro"])
        print("Bairro:", dados["bairro"])
        print("Cidade:", dados["localidade"])
        print("Estado:", dados["uf"])

except:
    # Caso haja erro de conexão ou outro problema
    print("Falha ao consultar o CEP. Verifique sua conexão ou o número digitado.")