'''2 - Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação). Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.'''

def palindromo(texto):
    texto_limpo = "".join(c.lower() for c in texto if c.isalnum())
    return texto_limpo == texto_limpo[::-1]
frase = input("Digite uma frase: ")
resultado = palindromo(frase)
if resultado:
    print("Sim")
else:
    print("Não")