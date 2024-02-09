import requests
from bs4 import BeautifulSoup

url = 'Sent.html'

data = open(url, 'r').read()
soup = BeautifulSoup(data, 'html.parser')

texto = soup.find_all('div')



for i in texto: 
    if "Matricula:" in i.text:
        print(i)
    elif "Fecha de matriculación:" in i.text:
        print(i)
    elif "Color:" in i.text:
        print(i)
    elif "Marca:" in i.text:
        print(i)
    elif "Modelo:" in i.text:
        print(i)
    






