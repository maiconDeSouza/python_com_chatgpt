import json

dados = {"nome": "João", "idade": 30}

with open("arquivo.json", "w", encoding="utf-8") as f:
    json.dump(dados, f, ensure_ascii=False, indent=4)
