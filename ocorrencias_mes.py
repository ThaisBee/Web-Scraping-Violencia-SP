import requests
from bs4 import BeautifulSoup
import pandas as pd




def ocorrencias_mes(
    url: str,
    VIEWSTATE: str,
    EVENTVALIDATION: str,
    ANO: str,
    REGIAO: str,
    MUNICIPIO: str,
    DELEGACIA: int,
) -> pd.DataFrame:
    with requests.Session() as request_session:
        html = request_session.get(url).text
        soup = BeautifulSoup(html, "html.parser")
        data = {
            "__EVENTTARGET": "ctl00$conteudo$$btnMes",
            "__EVENTARGUMENT": "",
            "__LASTFOCUS": "",
            "__VIEWSTATE": VIEWSTATE,
            "__EVENTVALIDATION": EVENTVALIDATION,
            "ctl00$conteudo$ddlAnos": ANO,
            "ctl00$conteudo$ddlRegioes": REGIAO,
            "ctl00$conteudo$ddlMunicipios": MUNICIPIO,
            "ctl00$conteudo$ddlDelegacias": DELEGACIA,
        }

        request = request_session.post(url, data=data)
        soup = BeautifulSoup(request.content, "lxml")
        table = soup.find("table")
        df = pd.read_html(str(table))[0]
        return df
