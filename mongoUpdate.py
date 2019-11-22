import pymongo
import os

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "macTestDB"
COLLECTION_NAME = "macDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e
        
conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

#  update one field 
coll.update_one({'first':'PYnew'}, {'$set':{'last':'MIDIpro'} } )

# update many objs
coll.update_many({'first':'PYnew'}, {'$set':{'nationality':'ubuntu'} } )

documents = coll.find()

for doc in documents:
    print(doc)
    