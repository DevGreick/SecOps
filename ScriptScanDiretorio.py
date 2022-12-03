import requests
alvo = "https://www.terra.com.br/"
lista_tentativas = ["",".git", "login", "painel", "mail", ]
lista_tentativas2 = ["admin", "frameworks", "internal", "errors", "noticias"]
for tentativa in lista_tentativas:
 r = requests.get (alvo+tentativa)
 if r.status_code ==200:
  print( alvo+tentativa)
  for tentativa in lista_tentativas2:
    r = requests.get (alvo+tentativa)
 if r.status_code ==200:
  print( alvo+tentativa)