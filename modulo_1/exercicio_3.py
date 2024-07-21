"""
3. **Análise de Número**
- Escreva um programa que leia um número e informe se ele é positivo, negativo ou zero.
"""

print("Digite um número qualquer:")
number = int(input())

if number == 0:
    print("zero!")
elif number > 0:
    print("positivo!")
else:
    print("negativo!")
