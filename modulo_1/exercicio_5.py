"""
5. **Cálculo de IMC**
- Escreva um programa que leia a altura e o peso de uma pessoa e calcule o IMC (Índice de Massa Corporal). 
Em seguida, exiba se a pessoa está abaixo do peso, com peso normal ou acima do peso.
"""

indice = ["Abaixo do peso", "Peso normal", "Sobrepeso", "Obesidade"]


def calculo_imc(peso, altura):
    imc = round(peso / (altura * altura), 2)
    return imc


def resultado_imc(imc):
    if imc > 29.9:
        return f"Seu imc se é de {imc} e você está na faixa da Obesidade"

    if imc > 24.9:
        return f"Seu imc se é de {imc} e você está na faixa do Sobrepeso"

    if imc > 18.5:
        return f"Seu imc se é de {imc} e você está na faixa do Peso Normal. Parabéns!"

    if imc > 0:
        return f"Seu imc se é de {imc} e você está na faixa Abaixo do peso"

    if imc <= 0:
        return f"Valor inexistente"


print("Digite seu peso em quilos. Ex.: 88.90kg:")
peso = float(input())

print("Digite sua altura em metros. Ex.: 1.75")
altura = float(input())

imc = calculo_imc(peso, altura)
resultado = resultado_imc(imc)

print(resultado)
