import csv
from utils.mongo import getConnectionTo


def syncFile(path):
    dataset = []

    db = getConnectionTo("products")

    with open(path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            dict = {
                "title": row[0],
                "price": row[1],
                "link": row[2],
                "image_url": row[3]
            }
            dataset.append(dict)

        x = db.insert_many(dataset)
        print(x)
