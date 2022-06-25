from web.ScrapperInterface import ScrapperInterface
from utils.request import makeRequest
from bs4 import BeautifulSoup
import csv


class Mesajil(ScrapperInterface):

    def __init__(self, url):
        self.url = url
        self.source = "Mesajil"
        self.products = []
        self.output_data = []

    def getCatalog(self, soup):
        return soup.find("div", class_="products")

    def getProducts(self, catalog):
        return catalog.find_all("div", class_="product-grid-item")

    def getProductTitle(self, product):
        return product.find("h3", class_="wd-entities-title").text.strip()

    def getProductImage(self, product):
        return product.find("img")['src']

    def getProductPrice(self, product):
        raw_price = product.find("span", class_="woocommerce-Price-amount")
        return raw_price.text.replace("S/", "").strip()

    def getProductLink(self, product):
        return product.find('a')['href']

    def fetchData(self):
        page = makeRequest(self.url)
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
        with open('mesajil.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(self.output_data)

    def run(self):
        self.parseScrappedData(self.fetchData())
        self.saveToFile()
