from bson import ObjectId
import pymongo
from pymongo import MongoClient

client = MongoClient("localhost",27017) #MongoClient("localhost:27017")
db = client.jobapp  #db = client['jobapp']
collections = db.users

users = collections.find()
for user in users:
    print(user)
    
users = collections.find({"name":"item"})
for user in users:
    print(user)

users = collections.find({"age":{"$lt":30}})
for user in users:
    print(user)
    
users = collections.find({"age":{"$lt":30}},{"name":1,"city":1,"_id":0})
for user in users:
    print(user)

users = collections.find().sort("age",-1)
for user in users:
    print(user)

pipeline = [
    {
        "$sort":{"$lastApplication":1}
    },
    {
        "_$group":{
            "$id":"$city",
            "job_post_count":{'$sum':1},
            "firstApplicatio":{'$first':"$lastApplication"}
        }
    }
]
results = collections.aggregate(pipeline)
print(results)

user = {
  "name": "Inserted from Python",
  "age": 23,
  "city": "San Jose, United States",
  "location": [
    40.6892,
    74.0445
  ],
  "hobbies": [
    "Dancing"
  ],
  "education": {
    "university": "Calfornia university",
    "start": "02-2015",
    "end": "02-2016",
    "degree": "BBA"
  },
  "lastApplication": {
    "$date": {
      "$numberLong": "1647335100000"
    }
  }
}
inserted = collections.insert_one(user)
print(inserted)

new_users = [{"name":"aaaa","age":11},{"name":"artorias","age":12}]
inserteds = collections.insert_many(user)
print(inserteds)

collections.delete_one({"_id":ObjectId("ID")})
collections.delete_many({"age":{"$gt":40}})

collections.update_one({"name":"aaaa"},{"$set":{"name":"arkhane"}})
collections.update_many({"name":"aaaa"},{"$set":{"name":"undefined"}})