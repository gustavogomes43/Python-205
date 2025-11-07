'''3 - Criar um código que serve para verificar se uma senha digitada pelo usuário atende a critérios básicos de segurança.
a - deve ter pelo menos 8 caracteres.
b - deve conter pelo menos um número.'''

'''senha = input("Digite uma senha: ")
tamanho_senha = len(senha) >= 8
numero_senha = any(s.isdigit() for s in senha)
if tamanho_senha and numero_senha:
    print("Senha Válida")
else:
    print("Senha inválida")'''

def validar_senha(senha):
    return len(senha) >= 8 and any(s.isdigit() for s in senha)
senha = input("Digite uma senha: ")
while not validar_senha(senha):
    print("Senha inválida, Tente outra.")
    senha = input("Digite uma senha: ")
print("Senha correta.")
