# Programa que lê um arquivo informado pelo usuário e mostra seu conteúdo

# pede o nome do arquivo ao usuário
nome_arquivo = input("Digite o nome do arquivo que deseja ler (ex: pessoas.txt): ")

try:
    # tenta abrir o arquivo no modo leitura
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        print("\n--- Conteúdo do arquivo ---\n")
        # percorre cada linha do arquivo
        for linha in arquivo:
            # remove quebras de linha extras e exibe
            print(linha.strip())

except FileNotFoundError:
    print("Erro: o arquivo informado não foi encontrado.")
except Exception as e:
    print("Ocorreu um erro ao tentar ler o arquivo:", e)