'''1 - Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/).'''

'''numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
operacao = input("Digite a operação desejada (+, -, *, /): ")
if operacao == "+":
    print(numero1 + numero2)
elif operacao == "-":
    print(numero1 - numero2)
elif operacao == "*":
    print(numero1 * numero2)
elif operacao == "/":
    print(numero1 / numero2)
else:
    print("Operação inválida!")'''

def calculadora(numero1, operacao, numero2):
    if operacao == "+":
        return numero1 + numero2
    elif operacao == "-":
        return numero1 - numero2
    elif operacao == "*":
        return numero1 * numero2
    elif operacao == "/":
        return numero1 / numero2
    else:
        return "Operação inválida!"
num1 = int(input("Digite o primeiro número: "))
oper = input("Digite a operação desejada (+, -, *, /): ")
num2 = int(input("Digite o segundo número: "))

print(calculadora(num1, oper, num2))

    
