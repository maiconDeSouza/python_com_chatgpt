import re

texto = "O rato roeu a roupa do rei de Roma."
padrao = r'r\w+'
resultados = re.findall(padrao, texto)
print(resultados)
