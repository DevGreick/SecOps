import requests
alvo = "http://pudim.com.br/"
lista_tentativas = ["",".git", "login", "painel", "mail"]
for tentativa in lista_tentativas:
 r = requests.get (alvo+tentativa)
if r.status_code ==200:
  print("encontrei ->", alvo+tentativa)
else:
  print("offline ->", alvo+tentativa)