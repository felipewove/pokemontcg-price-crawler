import requests
from bs4 import BeautifulSoup
from pokemontcgsdk import Card, Set, Subtype, Supertype, Type

col = Set.find('sm8')
print(vars(col))

collection = 'LTD'
url = "https://ligapokemon.com.br/?view=cards/search&card=ed={}&page=1".format(collection)
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
rows = soup.find('table', id='cotacao-busca').find_all('tr')

for row in rows[1:]:
    columns = row.find_all('td')
    print(">>>>>>>>>>>>>>>>>>>")
    print("Nome: ", row.find(class_='preto').string)
    print("Preco menor: ", row.find(class_='preMen').string)
    print("Preco medio: ", row.find(class_='preMed').string)
    print("Preco maior: ", row.find(class_='preMai').string)
