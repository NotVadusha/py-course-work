import os
import tkinter
from classes.master import master
from classes.client import client
from classes.service import service
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv


load_dotenv()
db = MongoClient(os.getenv("MONGO_URI"))

try:
    db.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

dblist = db.list_database_names()
if 'classes_db' in dblist:
    print('db exists')
else:
    masters = db["classes_db"]["classes_collection"]
    clients = db["classes_db"]["classes_collection"]
    services = db["classes_db"]["classes_collection"]

while True:
    inp = input("Select\n")
    if inp == 'q':
        break

