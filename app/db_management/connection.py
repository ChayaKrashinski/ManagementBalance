from enum import Enum
from pymongo import MongoClient

client=MongoClient()

client = MongoClient("localhost", 27017)
db = client["managementBalance"]
users = db['users']
