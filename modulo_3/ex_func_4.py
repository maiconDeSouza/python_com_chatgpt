"""
4. **Função com Retorno de Múltiplos Valores**
   - Crie uma função que receba um número e retorne o quadrado e o cubo desse número.
"""

def quadrado_cubo(numero):
    quadrado = numero ** 2
    cubo = numero ** 3

    return (quadrado, cubo)

retorno = quadrado_cubo(3)

print(retorno)