import pymongo
import json

# Connect to the MongoDB database
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["test_database"]
collection = db["test_collection"]

# Retrieve data from the collection
data = list(collection.find({}))

# Convert data to a JSON string
json_data = json.dumps(data, default=str)

print(json_data)
