from datetime import datetime, timedelta

agora = datetime.now()
amanha = agora + timedelta(days=1)

print(agora)
print(amanha)

data_str = agora.strftime("%d-%m-%y")
print(data_str)
