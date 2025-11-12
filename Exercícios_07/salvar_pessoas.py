# Programa que cria um arquivo com dados de pessoas e salva em formato tabular

# pede o nome do arquivo ao usuário
nome_arquivo = input("Digite o nome do arquivo para salvar (ex: pessoas.txt): ")

# lista de pessoas (exemplo)
pessoas = [
    {"nome": "Ana", "idade": 25, "cidade": "São Paulo"},
    {"nome": "Bruno", "idade": 30, "cidade": "Rio de Janeiro"},
    {"nome": "Carla", "idade": 22, "cidade": "Belo Horizonte"},
    {"nome": "Diego", "idade": 28, "cidade": "Curitiba"}
]

try:
    # abre o arquivo no modo escrita
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        # escreve o cabeçalho
        arquivo.write("Nome\tIdade\tCidade\n")
        arquivo.write("-" * 30 + "\n")

        # escreve cada pessoa em uma linha
        for p in pessoas:
            arquivo.write(f"{p['nome']}\t{p['idade']}\t{p['cidade']}\n")

    print(f"Arquivo '{nome_arquivo}' salvo com sucesso!")

except Exception as e:
    print("Falha ao salvar o arquivo:", e)