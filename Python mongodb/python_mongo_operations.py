#pymongo operations
from pymongo import MongoClient

# Establish a connection to MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Access a database
db = client['mydatabase']

# Access a collection
collection = db['mycollection']

# Insert a single document
document = {'name': 'John', 'age': 30}
collection.insert_one(document)

# Insert multiple documents
documents = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 35}]
collection.insert_many(documents)


# Find all documents in a collection
results = collection.find()

# Iterate over the results
for document in results:
    print(document)

# Find documents that match a specific condition
results = collection.find({'age': {'$gt': 30}})


# Update a single document
collection.update_one({'name': 'John'}, {'$set': {'age': 31}})

# Update multiple documents
collection.update_many({'age': {'$lt': 30}}, {'$inc': {'age': 1}})

# Delete a single document
collection.delete_one({'name': 'John'})

# Delete multiple documents
collection.delete_many({'age': {'$gt': 30}})
