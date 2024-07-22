"""
1. **Importação de Módulos Padrão**
   - Importe o módulo `math` e use a função `sqrt` para calcular a raiz quadrada 
   de um número. Exiba o resultado.
"""
import math

def raiz_quadrada(numero):
    return f"A raiz Quadrada de {numero} é {math.sqrt(numero)}"

resultado = raiz_quadrada(712)

print(resultado)