# **Anotações Projeto Busca Veiculos**

## Anotações

### Pandas

```df.read_[csv / json / excel]('nomearquivo.extensão') ``` - para ler arquivos como um DataFrame Pandas

```df.to_[csv / json / excel]('nomearquivo.extensão')``` - Para salvar um DataFrame Pandas em csv,json ou excel

```df.values()``` - retorna todos os valores contidos no DataFrame

```len(df.values())``` Retorna a quantidade de registros(linhas) contidas no DataFrame

```pd.DataFrame.from_dict('Nome dicionario ou lista contendo dicionarios')``` - Converte Dicionarios python para DataFrames Pandas

### Git

```git status``` - Verifica a situação atual do repositorio

```git add (nome arquivos)``` - Adicona Arquivos para o container antes de serem Commitados

```git commit -m "Mensagem de commit"``` - Realiza um Commit

```git push``` - Realiza a Sincronização do repositorio local com o origem (necessita de configuração previa)


## Bibliografia
> * [Guia Markdown](https://www.markdownguide.org/)
> * [Documentação Pandas](https://pandas.pydata.org/pandas-docs/stable/search.html?q=.unique)
> * [Como Concatenar DataFrames Pandas](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html)
> * [Remover Coluna index pandas salvando](https://stackoverflow.com/questions/26786960/remove-index-column-while-saving-csv-in-pandas)
> * [Setar uma coluna como o index Pandas DataFrame](https://datatofish.com/column-as-index-pandas-dataframe/)
> * [Como Adicionar e mover uma coluna para primeira Posição Pandas](https://www.geeksforgeeks.org/how-to-move-a-column-to-first-position-in-pandas-dataframe/)
> * [Concatenar DataFrame Pandas](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html)
