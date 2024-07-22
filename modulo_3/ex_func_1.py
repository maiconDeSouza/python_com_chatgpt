"""
1. **Função de Saudação**
   - Crie uma função que aceite um nome como argumento e retorne uma saudação 
   personalizada. Chame a função e exiba a saudação.
"""
def saudacao(*, saudacao="Olá", nome):
    return f"{saudacao}, {nome}"

print(saudacao(saudacao="Bom dia", nome="Dante"))
print(saudacao(nome="Monica"))