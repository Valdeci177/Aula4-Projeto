# Definindo a senha
senha_cadastrada = "1234"

# Inicializando o celular
print("Inicializando o celular...")

# Loop para solicitar a senha ao usuário
for tentativa in range(3, 0, -1):  # Inicia com 3 tentativas e decrementa até 1
    senha = input("Por favor, insira a senha: ")

    # Verificando se a senha está correta
    if senha == senha_cadastrada:
        print("Bem-vindo!")
        break  # Encerra o loop se a senha estiver correta
    else:
        if tentativa == 1:
            print("Senha incorreta. O celular será bloqueado.")
        else:
            print("Senha incorreta. Tentativas restantes:", tentativa - 1)

# Se todas as tentativas forem esgotadas, o celular é bloqueado
else:
    print("Todas as tentativas foram esgotadas. O celular está bloqueado.")