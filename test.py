import csv
import sys

import requests
from bs4 import BeautifulSoup
from util import split_name_code

# from pokemontcgsdk import Card, Set

writer = csv.writer(open("export.csv", "w", newline=""))

# collection = Set.find('sm8')

# LigaPokemon paginates by 30
# total_pages = int(collection.total_cards / 30) + 1

collection_arg = sys.argv[1]
current_page = 1
total_pages = None
url = "https://ligapokemon.com.br/?view=cards/search&card=ed={}&page={}"
while current_page:
    page = requests.get(url.format(collection_arg, current_page))
    soup = BeautifulSoup(page.content, "html.parser")
    # soup = BeautifulSoup(open("backup.html", "r"), 'html.parser')
    total_pages = int(soup.find("li", id="paginacao-1").b.contents[0]) / 30 + 1
    rows = soup.find("table", id="cotacao-busca").find_all("tr")
    # first row is table header, so ignore it
    for row in rows[1:]:
        splitted_name = split_name_code(row.find(class_="preto").string)
        content = {
            "name_pt": splitted_name["name_pt"],
            "name_en": splitted_name["name_en"],
            "code": splitted_name["code"],
            "price_min": row.find(class_="preMen").p.contents[0],
            "price_avg": row.find(class_="preMed").p.contents[0],
            "price_max": row.find(class_="preMai").p.contents[0],
        }
        writer.writerow(content.values())
    current_page = current_page + 1 if current_page <= total_pages else None
