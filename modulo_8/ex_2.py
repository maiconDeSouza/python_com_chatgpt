"""
#### Desafio 2: Expressões Regulares
- **Objetivo:** Crie um programa que leia um texto e substitua todas as
ocorrências de um número de telefone (no formato XXX-XXXX) por 'XXX-XXXX'.
- **Passos:**
  1. Leia um texto de entrada.
  2. Use uma expressão regular para encontrar e substituir números de telefone.
  3. Exiba o texto modificado.
"""

import re


def substituir_numeros_telefone(texto):
    return re.sub(r'\d{3}-\d{4}', 'XXX-XXXX', texto)


print("Digite o número a baixo")
numero = input()

print(substituir_numeros_telefone(numero))
