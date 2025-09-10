import request 
from bs4 import BeautifulSoup

url =  https://sp.senai.br/unidade/santanadeparnaiba
reponse = request.get(url)

soup = BeautifulSoup(response.text, "html.parser")

titulo = soup.title.string

print("Titulo da pagina",titulo)