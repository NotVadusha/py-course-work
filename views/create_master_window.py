from classes.master import *
from UI_primitives import *
from pymongo import *


def create_client_window(mongo: MongoClient):
    create_window = create_new_window("400x300")
    masters = mongo["classes_db"]["masters"]

    new_client = master()
    masters.insert_one(new_client)
