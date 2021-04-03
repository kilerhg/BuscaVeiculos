import requests
from bs4 import BeautifulSoup
import pandas as pd

'''
Funções para definir:

buscar site e converter para objetivo Bs4
achar os dados de interesse e retornar
limpar dados e separar em lista
transformar em database pandas e retornar
salvar em Excel
Salvar csv
ler em excel e retornar
ler em csv e retornar
'''

'''
Testes:

Entrar no site de veiculos e fazer webscraping basico
limpar dados
ler e salvar arquivo em CSV & Excel com pandas

'''

def BuscarSite():
    url = 'https://www.icarros.com.br/ache/listaanuncios.jsp?bid=0&opcaocidade=1&foa=1&cidadeaberto=&escopo=2&anunciosUsados=1&marca1=0&modelo1=&anomodeloinicial=0&anomodelofinal=0&locationSop=est_SP.1_-cid_9432.1_-esc_2.1_-rai_50.1_'
    resposta = requests.get(url).content
    site = BeautifulSoup(resposta,'html.parser')
    return site

def LimparDados(site):
    lista_veiculos = site.find('ul',attrs={'class':'listavertical'})
    veiculo = lista_veiculos.find_all('li',attrs={'anuncio anuncio_1ª_prioridade'})
    print(veiculo[0].prettify())
    

LimparDados(BuscarSite())