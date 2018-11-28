import csv
import sys

import requests
from bs4 import BeautifulSoup
# from pokemontcgsdk import Card, Set


def parse_names(names):
    splitted_names = names.split(' / ')
    name_pt = splitted_names[0]
    name_en = splitted_names[1] if len(splitted_names) > 1 else ''
    return name_pt, name_en


def split_name_code(name_ligapokemon):
    names = name_ligapokemon.split(' (')[0]
    name_pt, name_en = parse_names(names)

    code = name_ligapokemon.split(' (')[1][:-1]

    return {
        "name_pt": name_pt,
        "name_en": name_en,
        "code": code
    }


writer = csv.writer(open('export.csv', 'w', newline=''))

# collection = Set.find('sm8')

# LigaPokemon paginates by 30
# total_pages = int(collection.total_cards / 30) + 1

collection_arg = sys.argv[1]
url = "https://ligapokemon.com.br/?view=cards/search&card=ed={}&page=1".format(collection_arg)
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
# soup = BeautifulSoup(open("backup.html", "r"), 'html.parser')

rows = soup.find('table', id='cotacao-busca').find_all('tr')
# first row is table header, so ignore it
for row in rows[1:]:
    splitted_name = split_name_code(row.find(class_='preto').string)
    content = {
        'name_pt': splitted_name['name_pt'],
        'name_en': splitted_name['name_en'],
        'code': splitted_name['code'],
        'price_min': row.find(class_='preMen').p.contents[0],
        'price_avg': row.find(class_='preMed').p.contents[0],
        'price_max': row.find(class_='preMai').p.contents[0]
    }
    writer.writerow(content.values())
