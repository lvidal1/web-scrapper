from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(
    "mongodb+srv://root:z5lcBTFthHZiDsGn@products.fvdt9jr.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))

db = client["scrapped_products"]

col = db["test"]

collist = db.list_collection_names()
if "test" in collist:
    print("The collection exists.")

    dict = {"name": "Leo", "address": "Av. Camera Man"}
    x = col.insert_one(dict)
