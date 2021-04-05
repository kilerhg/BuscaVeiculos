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
'''
<h2 class="esquerda titulo_anuncio">
<h3 class="direita preco_anuncio">
div class="dados_veiculo"
div class="dados_anunciante"
'''

"""
    print(f'''
    Titulo Anuncio - {nome_veiculo}
    Valor Veiculo  - {valor_veiculo}
    Ano modelo     - {ano_modelo}
    Km Rodados     - {km_rodado}
    Cor            - {cor}
    cambio         - {cambio}
    descricao      - {descricao_anuncio}
    ''')
"""

def BuscarSite():
    url = 'https://www.icarros.com.br/ache/listaanuncios.jsp?bid=0&opcaocidade=1&foa=1&cidadeaberto=&escopo=2&anunciosUsados=1&marca1=0&modelo1=&anomodeloinicial=0&anomodelofinal=0&locationSop=est_SP.1_-cid_9432.1_-esc_2.1_-rai_50.1_'
    resposta = requests.get(url).content
    site = BeautifulSoup(resposta,'html.parser')
    return site

def LimparDados(site):
    lista_veiculos = site.find('ul',attrs={'class':'listavertical'})
    veiculos = lista_veiculos.find_all('li',attrs={'anuncio anuncio_1ª_prioridade'})
    for veiculo in veiculos:
        nome_veiculo = veiculo.find('h2',attrs={'class':'esquerda titulo_anuncio'}).text.strip()
        valor_veiculo = veiculo.find('h3',attrs={'class':'direita preco_anuncio'}).text[3:-13].strip()

        informacoes_veiculo = veiculo.find('div',attrs={'class':'dados_veiculo'}).find_all('p')
        ano_modelo = str(informacoes_veiculo[0].text).replace(' ','')
        ano_modelo = ano_modelo[:5] + ano_modelo[-4:]
        km_rodado = informacoes_veiculo[1].text.strip()
        cor = informacoes_veiculo[2].text.strip()
        cambio = informacoes_veiculo[3].text.strip()
        descricao_anuncio = informacoes_veiculo[4].text.strip()

        informacoes_anunciante = veiculo.find('div',attrs={'class':'dados_anunciante'}).find_all('p')
        bairro = informacoes_anunciante[0].text
        cidade, uf = informacoes_anunciante[1].find_all('span')
        cidade, uf = cidade.text, uf.text
        print()
        print(f'''
        Titulo Anuncio - {nome_veiculo}
        Valor Veiculo  - {valor_veiculo}
        Ano modelo     - {ano_modelo}
        Km Rodados     - {km_rodado}
        Cor            - {cor}
        cambio         - {cambio}
        descricao      - {descricao_anuncio}
        ''')

LimparDados(BuscarSite())