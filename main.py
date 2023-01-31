from gid import GetInicialData
from ocorrencias_mes import ocorrencias_mes
import pandas as pd


def main():
    inicial_data = GetInicialData()
    inicial_data.get_data_fom_web()
    dict_anos = inicial_data.dict_anos
    dict_regioes = inicial_data.dict_regioes
    dict_municipios = inicial_data.dict_municipios
    dict_delegacias = inicial_data._delegacias
    url = inicial_data.url
    VIEWSTATE = inicial_data.viewstate
    EVENTVALIDATION = inicial_data.eventvalidation

    # Constantes para o request
    # Consulte o disiconarios:
    # dict_anos, dict_regioes, dict_municipios, dict_delegacia
    # para saber as informações correspondentes aos números passados

    ANO = "2022"
    REGIAO = "1"
    MUNICIPIO = "1"
    DELEGACIA = 1410

    df = ocorrencias_mes(
        url,
        VIEWSTATE,
        EVENTVALIDATION,
        ANO,
        REGIAO,
        MUNICIPIO,
        DELEGACIA,
    )

    print(df)


if __name__ == "__main__":
    main()
