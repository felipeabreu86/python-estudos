from helpers.string_helper import StringHelper


def collatz(number):
    result = (number // 2) if (number % 2 == 0) else (3 * number + 1)
    print(result)
    return result


num_input = ""

while True:
    num_input = input("Insira um número inteiro maior que 1: ")
    if StringHelper.is_int(num_input) and int(num_input) > 1:
        num_input = int(num_input)
        break
    else:
        print("Número inválido. Tente novamente.")


while num_input != 1:
    num_input = collatz(num_input)
