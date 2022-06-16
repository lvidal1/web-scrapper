import requests
from bs4 import BeautifulSoup

URL = "https://platanitos.com/catalogo?breadcrumbs[]=Moda%20-%20mujeres%20%3E%20Zapatos%20%3E%20Sandalias&sort=timestamp_active+desc"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

catalog = soup.find("div", class_="container-catalog-responsive")
products = catalog.find_all("div", class_="nd-ct__item")

for product in products:
    image_element = product.find("img", class_="swiper-lazy nd-ct__img")
    title_element = product.find("p", class_="nd-ct__item-title")
    prices_element = product.find("p", class_="nd-ct__item-prices")
    price_element = prices_element.find("label")
    print(title_element.text.strip())
    print(image_element['src'])
    print(price_element.text.strip())
