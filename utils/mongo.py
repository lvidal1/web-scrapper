from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Client connection
# It is secured by network access :)


def getClient():
    client = MongoClient(
        "mongodb+srv://root:z5lcBTFthHZiDsGn@products.fvdt9jr.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))

    return client["scrapped_products"]


def getConnectionTo(table):
    return getClient()[table]


# def connectToCollection()


# collist = db.list_collection_names()


# if "test" in collist:
#     print("The collection exists.")

#     dict = {"name": "Leo", "address": "Av. Camera Man"}
#     x = col.insert_one(dict)
