'''2 - Criar um código que registre as notas de alunos e calcular a média da turma.'''

'''alunos = int(input("Digite a quantidade de alunos para a média de notas: "))
soma = 0
for i in range(alunos):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    soma += nota
print("A média de nota dos alunos é:", soma / alunos)'''

def media_alunos(quantid):
    soma = 0
    for i in range(quantid):
        soma += float(input(f"Digite a nota do aluno {i+1}: "))
    return soma / quantid
quant = int(input("Digite a quantidade de alunos para a média de notas: "))
print("A média de nota dos alunos é:", media_alunos(quant))