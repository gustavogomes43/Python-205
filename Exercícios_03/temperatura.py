# Definindo as fórmulas de conversão (com precisão de 273.15)

def c_to_f(celsius):
    """Converte Celsius para Fahrenheit."""
    return (celsius * 9/5) + 32

def f_to_c(fahrenheit):
    """Converte Fahrenheit para Celsius."""
    return (fahrenheit - 32) * 5/9

def c_to_k(celsius):
    """Converte Celsius para Kelvin."""
    return celsius + 273.15

def k_to_c(kelvin):
    """Converte Kelvin para Celsius."""
    return kelvin - 273.15

def f_to_k(fahrenheit):
    """Converte Fahrenheit para Kelvin."""
    # Primeiro converte para Celsius, depois para Kelvin
    celsius = f_to_c(fahrenheit)
    return c_to_k(celsius)

def k_to_f(kelvin):
    """Converte Kelvin para Fahrenheit."""
    # Primeiro converte para Celsius, depois para Fahrenheit
    celsius = k_to_c(kelvin)
    return c_to_f(celsius)

def conversor_temperatura():
    """
    Solicita a temperatura, unidades de origem e destino, e realiza a conversão.
    """
    print(" Conversor de Temperatura (C, F, K) ")
    print("-" * 50)

    # 1. Obter a temperatura e a unidade de origem
    try:
        temp = float(input("Digite a temperatura: "))
    except ValueError:
        print("\n Erro: Por favor, insira um valor numérico válido para a temperatura.")
        return

    unidades = {'c': 'Celsius', 'f': 'Fahrenheit', 'k': 'Kelvin'}
    
    # Solicita e valida a unidade de origem
    while True:
        unidade_origem_str = input("Unidade de origem (C/F/K): ").lower()
        if unidade_origem_str in unidades:
            unidade_origem = unidade_origem_str
            break
        print(" Unidade de origem inválida. Use C, F ou K.")

    # Solicita e valida a unidade de destino
    while True:
        unidade_destino_str = input("Unidade de destino (C/F/K): ").lower()
        if unidade_destino_str in unidades:
            unidade_destino = unidade_destino_str
            break
        print(" Unidade de destino inválida. Use C, F ou K.")
    
    # Se as unidades forem iguais, não há conversão a ser feita
    if unidade_origem == unidade_destino:
        resultado = temp
        funcao_conversao = None # Indica que não houve conversão
    else:
        # 2. Realizar a conversão usando as funções
        
        # Estratégia: Converte a origem para Celsius (se necessário) e depois para o destino
        
        # Passo 1: Converter a origem para Celsius (C), se não for C
        if unidade_origem == 'f':
            temp_em_c = f_to_c(temp)
        elif unidade_origem == 'k':
            temp_em_c = k_to_c(temp)
        else: # Já está em Celsius
            temp_em_c = temp
            
        # Passo 2: Converter de Celsius (C) para a unidade de destino
        if unidade_destino == 'f':
            resultado = c_to_f(temp_em_c)
            funcao_conversao = "C -> F"
        elif unidade_destino == 'k':
            resultado = c_to_k(temp_em_c)
            funcao_conversao = "C -> K"
        else: # Destino é C
            resultado = temp_em_c
            funcao_conversao = None # Já foi convertido para C no passo 1

    # 3. Apresentar os resultados
    print("-" * 50)
    print(f" Temperatura Original: **{temp:.2f} {unidade_origem.upper()} ({unidades[unidade_origem]})**")
    
    if funcao_conversao:
        print(f" Conversão ({unidade_origem.upper()} -> {unidade_destino.upper()})...")
    
    print(f" Resultado da Conversão: **{resultado:.2f} {unidade_destino.upper()} ({unidades[unidade_destino]})**")
    print("-" * 50)

# Chamar a função principal para rodar o programa
if __name__ == "__main__":
    conversor_temperatura()

