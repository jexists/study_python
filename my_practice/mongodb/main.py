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

# 삽입하기
def insert_test_doc():
  collection = test_db.test
  test_document = {
    "name": "joy",
    "type": "test"
  }
  insert_id = collection.insert_one(test_document).inserted_id
  print(insert_id)
# insert_test_doc()

production = client.production
person_collection = production.person_collection

def create_docments():
  first_names = ["joy", "sad"]
  last_names = ["J", "H"]
  ages = [21, 24]

  docs = []
  for first_name, last_name, age in zip(first_names, last_names, ages):
    doc = {
      "first_name": first_name,
      "last_name": last_name,
      "age": age,
    }
    docs.append(doc)
  person_collection.insert_many(docs)

create_docments()