import sys

import requests
from bs4 import BeautifulSoup
# from pokemontcgsdk import Card, Set

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
    columns = row.find_all('td')
    print(">>>>>>>>>>>>>>>>>>>")
    print("Nome: ", row.find(class_='preto').string)
    print("Preco menor: ", row.find(class_='preMen').p.contents[0])
    print("Preco medio: ", row.find(class_='preMed').p.contents[0])
    print("Preco maior: ", row.find(class_='preMai').p.contents[0])
