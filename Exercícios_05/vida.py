'''4 - Crie um programa que calcule a quantos dias um individuo está vivo de acordo com a data do dia.'''

from datetime import datetime

dia = int(input("Digite seu dia de nascimento: "))
mes = int(input("Digite seu mês de nascimento: "))
ano = int(input("Digite seu ano de nascimento: "))

nascimento = datetime(ano, mes, dia)
hoje = datetime.now()
vivo = (hoje - nascimento).days

print("Você já viveu", vivo, "dias.")