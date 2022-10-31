import pymongo


client = pymongo.MongoClient("mongodb+srv://testmongodb:test@cluster0.blxm1ta.mongodb.net/?retryWrites=true&w=majority")
db = client.test



print(db)

d = {
    "name" : "saurabh",
    "email":"srvsharma00@gmail.com",
    "surname":"kumar"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
