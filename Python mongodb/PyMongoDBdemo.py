#mongodb check the pymongo connection
from pymongo import MongoClient

#client = MongoClient('localhost',27017)
client = MongoClient("mongodb://localhost:27017/")
print(client.list_database_names())