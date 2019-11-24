import csv
import datetime
import sys
from math import ceil

import requests
from bs4 import BeautifulSoup

from util import parse_price, split_name_code

timestamp = datetime.datetime.now().strftime("%Y-%m-%d")

url = "https://ligapokemon.com.br/?view=cards/search&card=ed={}&page={}"

for collection_arg in sys.argv[1:]:
    current_page = 1
    total_pages = None
    writer = csv.writer(open(f"exports/export_{timestamp}_{collection_arg}.csv", "w"))
    while current_page:
        page = requests.get(url.format(collection_arg, current_page))
        soup = BeautifulSoup(page.content, "html.parser")
        if not total_pages:
            total_pages = ceil(int(soup.find(id="paginacao-1").b.contents[0]) / 30)
        # soup = BeautifulSoup(open("backup.html", "r"), "html.parser")

        rows = soup.find("table", id="cotacao-busca").find_all("tr")
        # first row is table header, so ignore it
        for row in rows[1:]:
            splitted_name = split_name_code(row.find(class_="preto").string)
            content = {
                "name_pt": splitted_name["name_pt"],
                "name_en": splitted_name["name_en"],
                "code": splitted_name["code"],
                "price_min": parse_price(row.find(class_="preMen").p.contents[0]),
                "price_avg": parse_price(row.find(class_="preMed").p.contents[0]),
                "price_max": parse_price(row.find(class_="preMai").p.contents[0]),
            }
            writer.writerow(content.values())
        current_page = current_page + 1 if current_page < total_pages else None
