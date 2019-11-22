import pymongo
import os

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "macTestDB"
COLLECTION_NAME = "macDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e
        
def show_menue():
    print("")
    print("1.) Add a Record")
    print("2.) Find a Record by Name")
    print("3.) Edit a Record")
    print("4.) Delete a Record")
    print("5.) EXIT")
    print("")
    print("*****************************************")
    
    
    opt = input("Select an Option :")
    return opt
    
    
def main_loop():
    
    while True:
        opt = show_menue()
        if opt == "1":
            print("\tSelected (+)Add Record(+)")
        elif opt == "2":
            print("\tSelected (%)Find Record(%)")    
        elif opt == "3":
            print("\tSelected (^)Edit Record(^)")
        elif opt == "4":
            print("\tSelected (-)Delete Record(-)")
        elif opt == "5":
            print("\tSelected (x)EXIT(x)")
            print("\t\t(x)GoodBye(x)")
            print("*****************************************")
            conn.close()
            break
        else:
            print("Invalid Option")
        print("*****************************************")
                
        
conn = mongo_connect(MONGODB_URI)
coll = conn[DBS_NAME][COLLECTION_NAME]



main_loop()



# documents = coll.find()

# for doc in documents:
#     print(doc)
    