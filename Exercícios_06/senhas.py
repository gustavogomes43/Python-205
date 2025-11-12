'''1 - Crie um programa que gere senhas aleatórias com letras, números e símbolos e que o usuário  também escolha o tamanho da senha  para criar senhas seguras automaticamente.'''

import random
import string

# Programa para gerar senhas aleatórias
print("=== GERADOR DE SENHAS ===")

# Usuário escolhe o tamanho da senha
tamanho = int(input("Digite o tamanho da senha que deseja: "))

# Conjunto de caracteres (letras, números e símbolos)
caracteres = string.ascii_letters + string.digits + string.punctuation

# Gera a senha aleatória
senha = ''.join(random.choice(caracteres) for _ in range(tamanho))

# Mostra a senha gerada
print("\nSua senha gerada é:")
print(senha)