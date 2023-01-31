
# Dados Estatísticos do Estado de São Paulo

## Projeto 

Foi feito o Web Scraping para coletar dados da web sobre as estatísticas de violência de SP.

## Site usado para coletar os dados

* http://www.ssp.sp.gov.br/Estatistica/Pesquisa.aspx.

## Como utilizar o programa

As constantes:

* ANO
* REGIAO 
* MUNICIPIO
* DELEGACIA 

devem ser inseridas no arquivo main.py para gerar a tabela escolhida. 

Observação: Por enquanto o programa apenas gera tabelas com dados de frequência mensal.

## Linguagem de programação usada

* Python 3.11.0

## Requirements

* bs4==0.0.1
* lxml==4.9.2
* pandas==1.5.3
* requests==2.28.2
