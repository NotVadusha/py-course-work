import tkinter
from classes.master import master
from classes.client import client
from classes.service import service
from pymongo.mongo_client import MongoClient


uri = "mongodb+srv://vadimkbondarchuk:RKpLSaFCXgZ0A1uV@classes.zfqimdn.mongodb.net/?retryWrites=true&w=majority"
db = MongoClient(uri)

try:
    db.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

dblist = db.list_database_names()
if 'classes_db' in dblist:
    print('db exists')
else:
    collection = db["classes_db"]["classes_collection"]

