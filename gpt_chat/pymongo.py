import pymongo

# Connect to the MongoDB database
client = pymongo.MongoClient("mongodb://<host>:<port>/")

# Authenticate with a username and password
db = client["test_database"]
db.authenticate("<username>", "<password>")

# Access a collection in the database
collection = db["test_collection"]

# Perform operations on the collection
# ...