"""
**2. Métodos Estáticos e de Classe**
   - Crie uma classe `Calculadora` com um método estático `multiplicar` que recebe dois números e 
   retorna o produto deles. Adicione um método de classe `criar_calculadora` que retorna uma instância da 
   classe `Calculadora`.
"""


class Calculadora:

    def multiplicar(num1, num2):
        return num1 * num2

    def criar_calculadora():
        return Calculadora()


resultado = Calculadora.multiplicar(5, 3)
nova_calculadora = Calculadora.criar_calculadora()

print(resultado)
print(nova_calculadora)
