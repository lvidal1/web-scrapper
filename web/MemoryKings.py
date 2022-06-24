from web.ScrapperInterface import ScrapperInterface
import requests
from bs4 import BeautifulSoup
import csv


class MemoryKings(ScrapperInterface):

    def __init__(self, url):
        self.url = url
        self.source = "Memory Kings"
        self.products = []
        self.output_data = []

    def getCatalog(self, soup):
        return soup.find("ul", class_="products")

    def getProducts(self, catalog):
        return catalog.find_all("li")

    def getProductTitle(self, product):
        return product.find("div", class_="title").text.strip()

    def getProductImage(self, product):
        return product.find("img")['src']

    def getProductPrice(self, product):
        raw_price = product.find("div", class_="price")
        return raw_price.text.split("ó")[1].replace("S/", "").strip()

    def getProductLink(self, product):
        return product.find('a')['href']

    def fetchData(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, "html.parser")
        return self.getProducts(self.getCatalog(soup))

    def parseScrappedData(self, products):
        for product in products:

            row_product = [
                self.getProductTitle(product),
                self.getProductPrice(product),
                self.getProductLink(product),
                self.getProductImage(product),
            ]

            self.output_data.append(row_product)

    def saveToFile(self):
        header = ['Title', 'Price', 'Link', 'Image']
        with open('memory_kings.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(self.output_data)

    def run(self):
        self.parseScrappedData(self.fetchData())
        self.saveToFile()
