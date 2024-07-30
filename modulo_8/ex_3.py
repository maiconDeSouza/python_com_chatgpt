"""
#### Desafio 3: Manipulação de Data e Hora
- **Objetivo:** Crie um programa que pergunte ao usuário a data de nascimento e 
calcule quantos dias ele já viveu.
- **Passos:**
  1. Peça ao usuário para inserir sua data de nascimento.
  2. Converta a entrada do usuário para um objeto `datetime`.
  3. Calcule a diferença entre a data atual e a data de nascimento.
  4. Exiba o número de dias vividos.
"""

from datetime import datetime

print("Digite a data do seu nascimento neste formato DD/MM/AAAA")
data_nascimento = input()


def calcular_idade(data_nascimento):
    dia, mes, ano = map(int, data_nascimento.split("/"))
    data_nasc = datetime(ano, mes, dia)
    data_atual = datetime.now()

    dia, mes, ano = map(int, data_nascimento.split('/'))
    data_nasc = datetime(ano, mes, dia)

    hoje = datetime.now()

    idade = hoje - data_nasc
    anos = idade.days // 365
    print(f"{anos} anos")


calcular_idade(data_nascimento)
