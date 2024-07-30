"""
#### Desafio 1: Manipulação de Arquivos
- **Objetivo:** Crie um programa que leia um arquivo de texto, conte o número de palavras e escreva o resultado em outro arquivo.
- **Passos:**
  1. Leia o conteúdo de um arquivo de texto.
  2. Conte o número de palavras no conteúdo lido.
  3. Escreva o resultado em um novo arquivo de texto.
"""
res = ""
with open("ex_1.txt", "r") as f:
    res = f.read().split()


with open("ex_1_res.txt", "w", encoding="utf-8") as f:
    f.write(f"Total de palavras no texto é de {len(res)} palavras.")
