'''1- Classificador de Idade

Crie um programa que solicite a idade do usuário e classifique-o
em uma das seguintes categorias:

*Criança (0-12 anos),
*Adolescente (13-17 anos),
*Adulto (18-59 anos) ou
*Idoso (60 anos ou mais).'''

idade = int(input("Digite sua idade: "))
if idade >= 0 and idade <= 12:
    print("Categoria: Criança.")
elif idade >= 13 and idade <= 17:
    print("Categoria: Adolescente.")
elif idade >= 18 and idade <= 59:
    print("Categoria: Adulto.")
elif idade >= 60:
    print("Categoria: Idoso.")
else:
    print("Idade inválida!")