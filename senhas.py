import time

senha = "123"
usuario = "py"
tentativas = 0
bloqueio = False

while True:
    login_usuario = input("Insira o usuário ")

    while login_usuario != usuario:
        print("ta errado garai")
        login_usuario = input("Insira o usuário ")

    print("salve " + usuario)

    login_senha = input("Insira a senha ")

    while (login_senha != senha) and (tentativas < 3):
        tentativas += 1
        print("ta errado doidão")
        login_senha = input("Insira a senha ")

    if tentativas < 3:
        print("ta em casa patrão")
        break
    else:
        print("ta bloqueado patrão")
        bloqueio = True

    if bloqueio:
        print("aguarde alguns instantes meu nobre")

        for i in range(5, 0, -1):
            print(".")
            time.sleep(1)

        tentativas = 0
        bloqueio = False
