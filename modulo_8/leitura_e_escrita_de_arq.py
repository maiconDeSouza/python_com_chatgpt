with open("arquivo.txt", "w") as file:
    file.write('Olá, mundo!\n')


with open("arquivo.txt", "r") as file:
    res = file.read()
    print(res)
