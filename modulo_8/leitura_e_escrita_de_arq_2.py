with open('arquivo_2.txt', 'r', encoding="utf-8") as f:
    while True:
        linha = f.readline()
        if not linha:
            break
        print(linha, end='')
