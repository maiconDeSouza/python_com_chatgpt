def aplicar_funcao(func, argumento):
    return func(argumento)


def dobro(x):
    return x * 2


resultado = aplicar_funcao(dobro, 5)
print(resultado)
