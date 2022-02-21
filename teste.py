from ctypes import sizeof
import requests
import json

response_api = requests.get("https://www.balldontlie.io/api/v1/players")
info = json.loads(response_api.content)

#print(info)
maior_peso = 0
nome_jogador_mais_pesado = ''
for i in range(0, len(info['data'])):
  #print(info['data'][i]['weight_pounds'])
  peso = info['data'][i]['weight_pounds']
  if(type(peso) == int):
    if(peso > maior_peso):
      maior_peso = peso
      nome_jogador_mais_pesado = info['data'][i]["first_name"]
      sobrenome_jogador_mais_pesado = info['data'][i]["last_name"]

#print(maior_peso)
#print(nome_jogador_mais_pesado)
print("O jogador com mais peso é : " + (str)(nome_jogador_mais_pesado) +" " +
(str)(sobrenome_jogador_mais_pesado) + " e tem: " + (str)(maior_peso)+ " kg ")
