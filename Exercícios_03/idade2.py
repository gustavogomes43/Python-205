def classificar_idade():
    """
    Solicita a idade do usuário e a classifica em categorias.
    """
    print("🎂 Classificador de Faixa Etária 🎂")
    print("-" * 40)

    # 1. Solicitar a idade do usuário
    try:
        idade = int(input("Por favor, digite a sua idade: "))
    except ValueError:
        # Mensagem de erro caso a entrada não seja um número inteiro
        print("\n❌ Erro: Por favor, insira um número inteiro válido para a idade.")
        return # Encerra a função se houver erro na entrada

    # 2. Validar se a idade é um valor razoável
    if idade < 0 or idade > 150:
        print("\n⚠️ Aviso: A idade inserida parece ser irreal. Tente novamente com um valor entre 0 e 150.")
        return

    # 3. Determinar a classificação
    classificacao = ""

    if 0 <= idade <= 12:
        classificacao = "Criança"
    elif 13 <= idade <= 17:
        classificacao = "Adolescente"
    elif 18 <= idade <= 59:
        classificacao = "Adulto"
    # O cenário restante é para 60 anos ou mais
    else: # idade >= 60
        classificacao = "Idoso"

    # 4. Apresentar o resultado
    print("-" * 40)
    print(f"✅ Idade digitada: **{idade} anos**")
    print(f"⭐ Classificação: Você se enquadra na categoria **{classificacao}**.")
    print("-" * 40)

# Chamar a função para rodar o programa
if __name__ == "__main__":
    classificar_idade()