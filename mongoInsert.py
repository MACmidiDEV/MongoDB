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


# singel instert
new_doc = { 'first': 'single', 'last': 'ADD', 'dob': '21/11/2019', 'gender': 'f','hair_colour': 'Terminal','occupation': 'Editor', 'nationality': 'Linux' }
coll.insert(new_doc)            


# muilple Insert
new_docs = [
    { 'first': 'Many', 'Insert': 'Script', 'dob': '1/1/2009', 'gender': 'f','hair_colour': 'Terminal','occupation': 'Editor', 'nationality': 'Linux'},
    { 'first': 'PYnew', 'last': 'Script', 'dob': '2/11/2000', 'gender': 'm','hair_colour': 'Terminal','occupation': 'Editor', 'nationality': 'Linux'}
]
coll.insert_many(new_docs)


documents = coll.find()

for doc in documents:
    print(doc)
    
    