'''3 - Crie um programa que serve para calcular o preço final de um produto após aplicar um desconto percentual.
a - Cálculo de desconto: Calcula o valor do desconto baseado em uma porcentagem.
b - Preço final: Determina o novo preço após o desconto.
c - Formatação: Arredonda o resultado para 2 casas decimais (centavos).
d - Interação com usuário: Pede os valores necessários e mostra o resultado formatado.'''

valor_original = float(input("Digite o valor do porduto: "))
porc_desc = float(input("Digite a porcetagem de desconto: "))
desconto = valor_original * (porc_desc / 100)
valor_final = valor_original - desconto
print("Valor final do produto: R$", round(valor_final, 2))