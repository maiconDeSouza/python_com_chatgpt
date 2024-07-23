"""
**Exercício:**
- Crie um decorador que registre a execução de uma função com um timestamp.
"""

import time
from functools import wraps


def register_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        total_time = end_time - start_time
        print(f"Função '{func.__name__}' executada em {
              total_time:.2f} segundos.")
        return result
    return wrapper


@register_execution_time
def calcular_fatorial(n):
    if n == 0:
        return 1
    else:
        return n * calcular_fatorial(n - 1)


calcular_fatorial(5)
