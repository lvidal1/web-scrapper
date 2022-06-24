import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.memorykings.pe/resultados/rtx"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
catalog = soup.find("ul", class_="products")
products = catalog.find_all("li")


def format_price(raw_price):
    return raw_price.split("ó")[1].replace("S/", "").strip()


f = open('./data-memory-kings.csv', 'w')
writer = csv.writer(f)

for product in products:
    link_element = product.find('a')
    image_element = product.find("img")
    title_element = product.find("div", class_="title")
    price_element = product.find("div", class_="price")

    row_product = [
        title_element.text.strip(),
        link_element['href'],
        image_element['src'],
        format_price(price_element.text)
    ]

    print(row_product)
    writer.writerow(row_product)

f.close()
