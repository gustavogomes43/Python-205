'''3- Calculadora de Média Escolar
Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:

* Nota 1: 7.5
* Nota 2: 8.0
* Nota 3: 6.5
O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais.'''

nota_1 = 7.5
nota_2 = 8.0
nota_3 = 6.5
media = (nota_1 + nota_2 + nota_3) / 3
print("Notas do aluno:", nota_1, ",", nota_2, ",", nota_3)
print("Média final:", round(media, 2))