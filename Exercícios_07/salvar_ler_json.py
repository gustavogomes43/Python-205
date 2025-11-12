import json

# pede o nome do arquivo JSON ao usuário
nome_arquivo = input("Digite o nome do arquivo para salvar (ex: pessoa.json): ")

# pede os dados da pessoa
nome = input("Digite o nome da pessoa: ")
idade = input("Digite a idade: ")
cidade = input("Digite a cidade: ")

# cria um dicionário com os dados digitados
pessoa = {
    "nome": nome,
    "idade": idade,
    "cidade": cidade
}

# tenta salvar o dicionário em um arquivo JSON
try:
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(pessoa, arquivo, indent=4, ensure_ascii=False)
    print(f"\nArquivo '{nome_arquivo}' salvo com sucesso!")
except Exception as e:
    print("Falha ao salvar o arquivo:", e)

# tenta ler o mesmo arquivo e mostrar os dados
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