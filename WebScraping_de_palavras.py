import pandas as pd
import numpy as np
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

#html = urlopen("https://www.globo.com")
html = urlopen(
    "https://oglobo.globo.com/?utm_source=globo.com&utm_medium=header&utm_campaign=chamada_header")
bsObj = BeautifulSoup(html.read(), "html.parser")
titulos = []

for link in bsObj.find_all("h1"):

    titulos.append(link.text)  # Pega todos so links da pagina


# Separa todos os titulos e agrupa na variavel usando List Comprehension
resultadooficial = [(titulos[i].split()) for i in range(len(titulos))]


todos = []
resultado = []
nome = []
quantidade = []

for i in range(len(resultadooficial)):

    for i2 in range(len(resultadooficial[i])):

        todos.append(resultadooficial[i][i2])


for i in range(len(todos)):  # Percorre todos as palavras

    if(todos.count(todos[i]) > 0):  # Mostras palavras com mais de 2 palavras repetidas
        if(todos[i] == 'mais' or todos[i] == 'de' or todos[i] == 'a' or todos[i] == 'que' or todos[i] == 'o' or todos[i] == 'e' or todos[i] == 'do' or todos[i] == 'da' or todos[i] == 'por' or todos[i] == 'com' or todos[i] == 'na' or
           todos[i] == 'a' or todos[i] == 'no' or todos[i] == 'em' or todos[i] == 'para' or todos[i] == 'é' or todos[i] == 'se' or todos[i] == 'tem' or todos[i] == 'ao' or todos[i] == 'tem' or todos[i] == 'não' or todos[i] == 'sim' or
           todos[i] == 'diz' or todos[i] == 'sobre' or todos[i] == 'cita' or todos[i] == 'são' or todos[i] == 'os' or todos[i] == 'pela'):

            carro = ""
        else:
            # Adiciona todos os titulos dos sites a variavel nome
            nome.append(todos[i])
            # Adiciona a quantidade de vezes que o nome se repetiu
            quantidade.append(todos.count(todos[i]))


# pPegas as duas variaveis coom o nomes e quantidades e geram o data frame
lista_de_tuplas = list(zip(nome, quantidade))
df = pd.DataFrame(
    lista_de_tuplas,
    columns=['Nome', 'Quantidade']
)
df = df.drop_duplicates()  # Elimina as linhas duplicadas
# Coloca em ordem crescente
df = df.sort_values(by=['Quantidade'], ascending=False)
print(df)
df.to_csv("terceiro.csv", index=False)  # index=false remove o index


# Corrigir os problemas nesses link   https://stackoverflow.com/questions/5620263/using-an-http-proxy-python
# https://stackoverflow.com/questions/14143198/errno-10060-a-connection-attempt-failed-because-the-connected-party-did-not-pro
