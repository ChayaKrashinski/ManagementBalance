from enum import Enum
from pymongo import MongoClient

client=MongoClient()
client = MongoClient("localhost", 27017)

db = client["managementBalance"]
users = db['users']

class Collection(Enum):
    users = db['users'],
    expenses = db['expenses'],
    revenues = db['revenues']