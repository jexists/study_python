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

# create_docments()

printer = pprint.PrettyPrinter()

def find_all_people():
  people = person_collection.find()

  for person in people:
    printer.pprint(person)

# find_all_people()
def find_joy():
  tim = person_collection.find_one({"first_name":"joy"})
  printer.pprint(tim)
# find_joy()

def find_joy_by_name():
  tim = person_collection.find_one({"first_name":"joy", "last_name": "J"})
  printer.pprint(tim)

def count_all_people():
  # count = person_collection.find().count()
  # find().count() 변경됨 -> count_documents()
  count = person_collection.count_documents(filter={})
  print("num of people :", count)
# count_all_people()

# 63b43ad36a7d3b218b0a3961
def get_person_by_id(person_id):
  from bson.objectid import ObjectId
  _id = ObjectId(person_id)
  person = person_collection.find_one({"_id":_id})
  printer.pprint(person)

# get_person_by_id("63b43ad36a7d3b218b0a3961")