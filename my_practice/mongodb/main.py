# https://www.youtube.com/watch?v=UpsZDGutpZc
# pip install pymongo[srv]
# pip3 install 'pymongo[srv]'
# pip install python-dotenv
# python -m pip install 

# MongoDB for VS Code (VS Extension)

from dotenv import load_dotenv, find_dotenv

import os
import pprint
from pymongo import MongoClient

load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")

connection_stiring = f"mongodb+srv://jexists:{password}@tutorial.gd8iztq.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(connection_stiring)

dbs = client.list_database_names()
print(dbs)

test_db = client.test

collections = test_db.list_collection_names()
print(collections)