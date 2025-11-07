'''4- Verificador de Ano Bissexto
Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.
Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.'''

'''ano = int(input("Digite um ano para chegar se é bissexto: "))
bissexto = False
if ano % 400 == 0:
    bissexto = True
elif ano % 100 == 0:
    bissexto = False
elif ano % 4 == 0:
    bissexto = True
if bissexto:
    print("É bissexto.")
else:
    print("Não é bissexto.")'''

def bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
ano = int(input("Digite um ano: "))
if bissexto(ano):
    print("É bissexto")
else:
    print("Não é bissexto.")
