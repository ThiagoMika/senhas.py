import time

senha = "123"
usuario = "py"
tentativas = 0
bloqueio = False

while True:
    login_usuario = input("Insira o usuário ")

    while login_usuario != usuario:
        print("Este usuário não existe")
        login_usuario = input("Insira o usuário ")

    print("Olá " + usuario)

    login_senha = input("Insira a senha ")

    while (login_senha != senha) and (tentativas < 3):
        tentativas += 1
        print("Senha incorreta")
        login_senha = input("Insira a senha ")

    if tentativas < 3:
        print("Acesso Liberado")
        break
    else:
        print("Você está bloqueado!")
        bloqueio = True

    if bloqueio:
        print("Aguarde alguns instantes e tente novamente")

        for i in range(5, 0, -1):
            print(".")
            time.sleep(1)

        tentativas = 0
        bloqueio = False
