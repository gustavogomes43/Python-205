import json

# pede o nome do arquivo JSON ao usuário
nome_arquivo = input("Digite o nome do arquivo para salvar (ex: pessoa.json): ")

# cria um dicionário com dados de uma pessoa
pessoa = {
    "nome": "Ana",
    "idade": 25,
    "cidade": "São Paulo"
}

# tenta salvar o dicionário em formato JSON
try:
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(pessoa, arquivo, indent=4, ensure_ascii=False)
    print(f"Arquivo '{nome_arquivo}' salvo com sucesso!")
except Exception as e:
    print("Falha ao salvar o arquivo:", e)

# tenta ler o mesmo arquivo e exibir os dados
try:
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
        print("\n--- Dados lidos do arquivo JSON ---")
        print(f"Nome: {dados['nome']}")
        print(f"Idade: {dados['idade']}")
        print(f"Cidade: {dados['cidade']}")

except FileNotFoundError:
    print("Erro: o arquivo não foi encontrado.")
except Exception as e:
    print("Falha ao ler o arquivo:", e)