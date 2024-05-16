from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27014/")

db = client['managementBalance']
collection = db['users']

### save new user
user = {'name': 'sara', 'password': '789456123', 'mail': 'a@mail'}
collection.insert_one(user)

###call user from db
current_user = collection.find_one({'name':user['name'], 'password':user['password']})
###call all users from db
for user in collection.find():
    print(user)

### delete user from db
collection.delete_one({'name':'mira'})