import datetime
import getopt
import sys
from urllib.request import urlopen

import pandas as pd
from bs4 import BeautifulSoup


def get_incidents_dataframe(province):
    try:
        print('Scraping traffic incidents on ' + datetime.datetime.today().strftime('%d-%m-%Y') + '\n')
        url = find_all_incidents_link()
        url = filter_by_province(url, province)
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


def find_all_incidents_link():
    # buscar url
    url = 'http://infocar.dgt.es/etraffic/'
    html = urlopen(url)
    soup = BeautifulSoup(html, "lxml")
    incidents_link = soup.findAll('div', id='verIncidencias')[0].findNext('a', href=True)
    return url + incidents_link['href']


def filter_by_province(url, province):
    # concatenar filtres
    if province is None:
        return url
    else:
        return '%s&provIci=%s' % (url, province)


def dataset_to_csv(dataset):
    # exportar a csv
    date = datetime.datetime.today().strftime('%Y%m%d')
    dataset.to_csv('incidentes_' + date + '.csv', sep=',', encoding='UTF-8')


def main(argv):
    province = None
    try:
        opts, args = getopt.getopt(argv, "hp:", ["province="])
    except getopt.GetoptError:
        print('IncidentsScraper.py -p <province>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('IncidentsScraper.py -p <province>')
            sys.exit()
        elif opt in ("-p", "--province"):
            province = arg

    dataset = get_incidents_dataframe(province)
    print(dataset.to_string())
    dataset_to_csv(dataset)


if __name__ == "__main__":
    main(sys.argv[1:])
