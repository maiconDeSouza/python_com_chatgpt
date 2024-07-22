"""
3. **Função com Parâmetros Padrão**
   - Crie uma função que receba um número e um valor padrão de operação 
   (adicionar ou multiplicar). Se a operação não for especificada, deve 
   adicionar 5 ao número. Caso contrário, deve multiplicar o número por 2.
"""

def calculo(numero:float, operacao=("adicionar", "multiplicar")):
    if operacao == "adicionar":
        return numero + 5
    elif operacao == "multiplicar":
        return numero * 2
    else:
        return "Operação invalida"

resultado_1 = calculo(5, operacao="adicionar")
print(resultado_1)

resultado_2 = calculo(5, "multiplicar")
print(resultado_2)

resultado_3 = calculo(5, "texto")
print(resultado_3)