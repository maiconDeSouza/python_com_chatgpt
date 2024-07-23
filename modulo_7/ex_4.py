"""
**Exercício:**
- Crie um gerador que produza a sequência de Fibonacci até um determinado número.
"""


def fibonacci_generator(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b


for numero in fibonacci_generator(89):
    print(numero)
