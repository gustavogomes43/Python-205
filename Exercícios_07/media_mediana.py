'''1 -  Crie um programa que lê um arquivo CSV de  com a biblioteca , 
calcule e exiba a  e o  da coluna tempo_execucao, caso e o arquivo não exista ou houver erro na leitura, mostre uma mensagem de erro.'''


import csv
import statistics

# nome do arquivo CSV
arquivo = "dados1.csv"

try:
    tempos = []

    # tenta abrir o arquivo
    with open(arquivo, 'r', newline='', encoding='utf-8') as csvfile:
        leitor = csv.DictReader(csvfile)
        
        # percorre cada linha e pega o valor da coluna tempo_execucao
        for linha in leitor:
            if 'tempo_execucao' in linha and linha['tempo_execucao']:
                try:
                    tempos.append(float(linha['tempo_execucao']))
                except ValueError:
                    # ignora valores inválidos
                    pass

    if len(tempos) > 0:
        media = statistics.mean(tempos)
        mediana = statistics.median(tempos)
        print(f"Média do tempo de execução: {media:.2f}")
        print(f"Mediana do tempo de execução: {mediana:.2f}")
    else:
        print("Nenhum dado válido encontrado na coluna 'tempo_execucao'.")

except FileNotFoundError:
    print("Erro: o arquivo não foi encontrado.")
except Exception as e:
    print("Ocorreu um erro ao ler o arquivo:", e)