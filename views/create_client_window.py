from classes.client import *
from UI_primitives import *
from pymongo import *


def create_client_window(mongo: MongoClient):
    create_window = create_new_window("400x300")
    clients = mongo["classes_db"]["clients"]

    new_client = client()
    clients.insert_one(new_client)
