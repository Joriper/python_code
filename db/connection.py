from pymongo import *
import pymongo
from dotenv import load_dotenv
import os

try:
    load_dotenv()
    connection = MongoClient(os.environ['MONGO_CONNECTION'])
    database = connection[os.environ['MONGO_DATABASE']]
    items_collection = database[os.environ['ITEM_COLLECTION']]
    clock_collection = database[os.environ['CLOCK_COLLECTION']]

except pymongo.errors.ConnectionFailure as e:
    print(f"Error:{e}")