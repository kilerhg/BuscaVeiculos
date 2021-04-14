import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl

'''
Funções para definir:

buscar site e converter para objetivo Bs4 X
achar os dados de interesse e retornar X
limpar dados e separar em lista X
transformar em database pandas e retornar X
salvar em Excel & CSV & json X
ler em excel e retornar X
ler em csv e retornar X
ler em json e retornar X
ler arquivos e verificar total de linhas e retornar X
salvar arquivos os arquivos concatenando X
Salvar Link junto com os dados
limpar Duplicatas


'''

'''
Testes:

Entrar no site de veiculos e fazer webscraping basico X
limpar dados X
ler e salvar arquivo em CSV & Excel com pandas X

'''
'''
<h2 class="esquerda titulo_anuncio">
<h3 class="direita preco_anuncio">
div class="dados_veiculo"
div class="dados_anunciante"
a class="clearfix"
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

def BuscarSite(url):
    resposta = requests.get(url).content
    site = BeautifulSoup(resposta,'html.parser')
    return site

def LimparDados(site):
    lista_veiculos = site.find('ul',attrs={'class':'listavertical'})
    veiculos = lista_veiculos.find_all('li',attrs={'anuncio anuncio_1ª_prioridade'})
    lista_dos_veiculos = []

    for veiculo in veiculos:
        dict_veiculos = {}
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

        link_bruto = veiculo.find('a',attrs={'class':'clearfix'})
        link = 'https://www.icarros.com.br' + link_bruto['href']

        dict_veiculos['nome_veiculo'] = nome_veiculo
        dict_veiculos['valor_veiculo'] = valor_veiculo
        dict_veiculos['ano_modelo'] = ano_modelo
        dict_veiculos['km_rodado'] = km_rodado
        dict_veiculos['cor_veiculo'] = cor
        dict_veiculos['cambio_veiculo'] = cambio
        dict_veiculos['descricao_anuncio'] = descricao_anuncio
        dict_veiculos['link'] = link
        lista_dos_veiculos.append(dict_veiculos.copy())
        dict_veiculos.clear()

    return lista_dos_veiculos
def ConverterDicionarioParaPandas(lista):
    try:
        lista = list(lista)
    except Error as erro:
        print(f'Erro Convertendo dict para pandas {erro}')

    df = pd.DataFrame.from_dict(lista)
    return df

def SalvarExcel(df,nome='arquivo',valor_index=True):
    df.to_excel(f'{nome}.xlsx',index=valor_index)

def SalvarCsv(df,nome='arquivo',valor_index=True):
    df.to_csv(f'{nome}.csv',index=valor_index)

def SalvarJson(df,nome='arquivo',valor_index=True):
    df.to_json(f'{nome}.json',index=valor_index)

def LerExcel(nome='arquivo'):
    try:
        df = pd.read_excel(f'{nome}.xlsx')
    except:
        print('Erro ler excel')

    return df

def LerCsv(nome='arquivo'):
    try:
        df = pd.read_csv(f'{nome}.csv')
    except:
        print('Erro ler CSV')

    return df

def LerJson(nome='arquivo'):
    try:
        df = pd.read_json(f'{nome}.json')
    except:
        print('Erro ler Json')

    return df

def ContaLinhas(df):
    valor = len(df.values) + 1

    return valor

def ConcatenarDataFrames(df1,df2):
    colunas = ['nome_veiculo', 'valor_veiculo', 'ano_modelo', 'km_rodado',
       'cor_veiculo', 'cambio_veiculo', 'descricao_anuncio','link']
    conjunto = pd.concat([df1,df2])
    conjunto = conjunto[colunas]
    conta_linhas = len(df1.values) + len(df2.values)
    try:
        conjunto.insert(0,'numeros',range(0,conta_linhas))
    except:
        pass
    
    return conjunto

def RemoverDuplicatas(df):
    try:
        df = df.drop_duplicates(subset=['link'])
    except:
        pass

    return df




' MAIN '

""" url = 'https://www.icarros.com.br/ache/listaanuncios.jsp?bid=0&opcaocidade=1&foa=1&cidadeaberto=&escopo=2&anunciosUsados=1&marca1=0&modelo1=&anomodeloinicial=0&anomodelofinal=0&locationSop=est_SP.1_-cid_9432.1_-esc_2.1_-rai_50.1_'
dicionario_limpo = LimparDados(BuscarSite(url))
dados = ConverterDicionarioParaPandas(dicionario_limpo) """
dados_salvos = LerExcel()
dados_salvos = RemoverDuplicatas(dados_salvos)
SalvarExcel(dados_salvos)
""" novo_dado = ConcatenarDataFrames(dados,dados_salvos)
SalvarExcel(novo_dado,valor_index=False) """

""" SalvarExcel(dados) """


""" LimparDados(BuscarSite(url)) """

