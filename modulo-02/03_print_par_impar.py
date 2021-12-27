from helpers.string_helper import StringHelper


is_num = False

while not is_num:
    valor = input("Insira um número inteiro: ")
    if StringHelper.is_int(valor):
        is_num = True
        par_impar = "PAR" if int(valor) % 2 == 0 else "IMPAR"
        print(f"O valor {valor} é {par_impar}.")
    else:
        print("Número inválido. Tente novamente.")
