def calcular_imc():
    """
    Solicita peso e altura, calcula o IMC e fornece a classificação.
    """
    print("🤖 Calculadora de Índice de Massa Corporal (IMC) 🤖")
    print("-" * 50)

    # 1. Solicitar entrada do usuário e garantir que são números
    try:
        # Pede o peso em quilogramas (kg)
        peso = float(input("Digite o seu peso em kg (ex: 75.5): "))
        # Pede a altura em metros (m)
        altura = float(input("Digite a sua altura em metros (ex: 1.75): "))
    except ValueError:
        # Mensagem de erro caso a entrada não seja um número
        print("\n❌ Erro: Por favor, insira valores numéricos válidos para peso e altura.")
        return # Encerra a função se houver erro na entrada

    # Validação básica para garantir que os valores são positivos e razoáveis
    if peso <= 0 or altura <= 0:
        print("\n❌ Erro: Peso e altura devem ser valores positivos.")
        return

    # 2. Calcular o IMC
    # Fórmula do IMC: peso / (altura * altura)
    imc = peso / (altura ** 2)

    # 3. Determinar a classificação
    classificacao = ""

    # A tabela padrão de IMC é avaliada em ordem.
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25: # Isso significa que 18.5 <= imc < 25
        classificacao = "Peso normal"
    elif imc < 30: # Isso significa que 25 <= imc < 30
        classificacao = "Sobrepeso"
    else: # Isso significa que imc >= 30
        classificacao = "Obeso"

    # 4. Apresentar os resultados
    print("-" * 50)
    # Formata o IMC para ter apenas 2 casas decimais
    print(f"✅ Seu IMC é: **{imc:.2f}**")
    print(f"⭐ Classificação: **{classificacao}**")
    print("-" * 50)

# Chamar a função para rodar o programa
if __name__ == "__main__":
    calcular_imc()