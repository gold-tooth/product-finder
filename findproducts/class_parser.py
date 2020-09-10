import requests
from bs4 import BeautifulSoup

class Parser:
    def __init__(self):
        self.url = "http://www.obedix.ru/info/?news=3"
        self.products = []

    def perform(self):
        center_tag = self.soup().find('center')
        for h2 in center_tag.find_all('h2'):    
            one_table_tag = h2.parent.parent.find('table')
            for i, tr in enumerate(one_table_tag.find_all('tr')):
                if i == 0: continue 
                item = []

                for td in tr.find_all('td'):
                    item.append(td.text)
                self.products.append({
                    "name": item[0], 
                    "water": item[1].replace(",", "."), 
                    "proteins": item[2].replace(",", "."),
                    "fats": item[3].replace(",", "."),
                    "carbohydrates": item[4].replace(",", "."),
                    "kcal": item[5].replace(",", ".")
                })

    def data(self):
        return self.products

    def soup(self):
        return BeautifulSoup (self.html(), 'html.parser')

    def html(self):
        source = requests.get(self.url)
        return source.text
