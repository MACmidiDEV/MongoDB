import pymongo
import os

# python const. set password in .bashrc to pull from envVAR
# hidden never post to git
MONGODB_URI = os.getenv("MONGO_URI")

# MongoDB atlas params
DBS_NAME = "macTestDB"
COLLECTION_NAME = "macDB"

# function to connect to DB
def mongo_connect(url):
    try:
# pass Const. to open connection        
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e

# Configure function to QUERY DB with params        
conn = mongo_connect(MONGODB_URI)
coll = conn[DBS_NAME][COLLECTION_NAME]
# run calls to DB below.

# QUERY calls to DB 
documents = coll.find()
# displays querys from DB
for doc in documents:
    print(doc)
    
    