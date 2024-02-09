import requests
from bs4 import BeautifulSoup

url = 'Sent.html'

data = open(url, 'r').read()
soup = BeautifulSoup(data, 'html.parser')

texto = soup.find_all('div')

info = []

for i in texto: 
    if "Matricula:" in i.text:
        info.append(i)
    elif "Fecha de matriculación:" in i.text:
        info.append(i)
    elif "Color:" in i.text:
        info.append(i)
    elif "Marca:" in i.text:
        info.append(i)
    elif "Modelo:" in i.text:
        info.append(i)

data = info[-5:]

with open('info.txt', 'w') as f:
    for i in data:
        f.write(i.text + '\n')


    






