import requests
from bs4 import BeautifulSoup


class GetInicialData:
    def __init__(self) -> None:
        self._url = "http://www.ssp.sp.gov.br/Estatistica/Pesquisa.aspx"
        self._anos = "ctl00$conteudo$ddlAnos"
        self._regioes = "ctl00$conteudo$ddlRegioes"
        self._municipios = "ctl00$conteudo$ddlMunicipios"
        self._delegacias = "ctl00$conteudo$ddlDelegacias"
        self._VIEWSTATE = ""
        self._EVENTVALIDATION = ""
        self._dict_anos = {}
        self._dict_regioes = {}
        self._dict_municipios = {}
        self._dict_delegacias = {}

    def _creates_a_dictionary(self, soup: BeautifulSoup, name: str) -> dict:
        list = soup.find("select", {"name": name}).find_all("option")
        dictio = {x.text: x["value"] for x in list}
        return dictio

    def get_data_fom_web(self) -> None:
        with requests.Session() as request:
            html = request.get(self._url).text
            soup = BeautifulSoup(html, "html.parser")

            self._dict_anos = self._creates_a_dictionary(soup, self._anos)
            self._dict_regioes = self._creates_a_dictionary(soup, self._regioes)
            self._dict_municipios = self._creates_a_dictionary(soup, self._municipios)
            self._dict_delegacias = self._creates_a_dictionary(soup, self._delegacias)

            self._VIEWSTATE = soup.find(id="__VIEWSTATE")["value"]
            self._EVENTVALIDATION = soup.find(id="__EVENTVALIDATION")["value"]

    @property
    def viewstate(self) -> str:
        return self._VIEWSTATE

    @property
    def eventvalidation(self) -> str:
        return self._EVENTVALIDATION

    @property
    def dict_anos(self) -> dict:
        return self._dict_anos

    @property
    def dict_regioes(self) -> dict:
        return self._dict_regioes

    @property
    def dict_municipios(self) -> dict:
        return self._dict_municipios

    @property
    def dict_delegacias(self) -> dict:
        return self._dict_delegacias

    @property
    def url(self) -> str:
        return self._url
