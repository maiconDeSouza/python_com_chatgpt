try:
    file = open('arquivo.txt', 'r')
except FileNotFoundError:
    print("Arquivo não encontrado.")
finally:
    file.close()
