'''4 - Crie um programa que realize consultas a cotações de moedas em relação ao Real (BRL) usando a API AwesomeAPI, mostre valor atual, máxima, mínima e data/hora da última atualização, caso a moeda não existir ou houver erro na requisição, retorne uma mensagem de erro.'''

import urllib.request
import json

print("=== CONSULTA DE COTAÇÃO ===")

# Pede a moeda para o usuário (ex: USD, EUR, GBP)
moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper()

# Monta o endereço da API
url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

try:
    # Faz a requisição à API
    resposta = urllib.request.urlopen(url)
    dados = json.loads(resposta.read().decode())

    # Monta a chave esperada, ex: "USDBRL"
    chave = moeda + "BRL"

    # Verifica se a moeda existe na resposta
    if chave in dados:
        info = dados[chave]

        # Mostra as informações da moeda
        print(f"\n=== Cotação de {moeda} para BRL ===")
        print("Valor atual:", info["bid"])
        print("Máxima do dia:", info["high"])
        print("Mínima do dia:", info["low"])
        print("Última atualização:", info["create_date"])
    else:
        print("Moeda não encontrada. Verifique o código informado.")

except:
    # Em caso de erro de conexão ou API fora do ar
    print("Erro ao consultar a API. Verifique sua conexão com a internet.")