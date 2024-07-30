def dividir(x, y):
    if not isinstance(x, int) and not isinstance(y, int):
        raise ValueError("Digite apenas números inteiros.")
    elif y == 0:
        raise ValueError("O divisor não pode ser zero.")
    return x / y


try:
    print("Digite um número para ser o x (que será dividido)")
    x = int(input())

    print("Digite um número para ser o y (que será o divisor)")
    y = int(input())
except Exception as error:
    print(error)
    print("Tente de novo")

try:
    resultado = dividir(x, y)
    print(resultado)
except Exception as error:
    print(error)
    print("Tente de novo")
