from enum import Enum
from pymongo import MongoClient

client=MongoClient()
# client = MongoClient("localhost", 27017)
# db = client["managementBalance"]

# users = None
# def get_db():
#     client = MongoClient("localhost", 27017)
#     db = client["managementBalance"]
#     users = db['users'],
#     expenses = db['expenses'],
#     revenues = db['revenues']

client = MongoClient("localhost", 27017)
db = client["managementBalance"]
users = db['users']
print(users.find_one({'name':"sara"}))
# expenses = db['expenses'],
# revenues = db['revenues']