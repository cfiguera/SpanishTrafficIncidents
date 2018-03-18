import datetime
from urllib.request import urlopen

import pandas as pd
from bs4 import BeautifulSoup


def get_incidents_dataframe():
    url = 'http://infocar.dgt.es/etraffic/Incidencias?ca=&provIci=&caracter=acontecimiento&accion_consultar=Consultar' \
          '&IncidenciasRETENCION=IncidenciasRETENCION&IncidenciasPUERTOS=IncidenciasPUERTOS&IncidenciasMETEOROLOGICA' \
          '=IncidenciasMETEOROLOGICA&IncidenciasEVENTOS=IncidenciasEVENTOS&IncidenciasOTROS=IncidenciasOTROS' \
          '&IncidenciasRESTRICCIONES=IncidenciasRESTRICCIONES&ordenacion=provincia-ASC%2Cpoblacion-ASC '

    try:
        print('Scraping traffic incidents on ' + datetime.datetime.today().strftime('%d-%m-%Y') + '\n')
        html = urlopen(url)
        soup = BeautifulSoup(html, "lxml")

        # extract table headers
        headers = [th.getText().replace('\n', ' ').strip() for th in soup.findAll('tr', limit=1)[0].findAll('th')]

        # extract data rows
        data_rows = soup.findAll('tr')[2:]
        data = [[td.getText().replace('\n', ' ') for td in data_rows[i].findAll('td')] for i in range(len(data_rows))]
        dataset = pd.DataFrame(data, columns=headers)

        # extract cause from icon
        causes = [[img['alt'] for img in data_rows[i].findAll('img')] for i in range(len(data_rows))]
        dataset['TIPO / NIVEL'] = causes

        return dataset

    except ValueError as error:
        print(error)
        return 0


def dataset_to_csv(dataset):
    date = datetime.datetime.today().strftime('%Y%m%d')
    dataset.to_csv('incidentes_' + date + '.csv', sep=',', encoding='UTF-8')


if __name__ == "__main__":
    dataset = get_incidents_dataframe()
    print(dataset.to_string())
    dataset_to_csv(dataset)
