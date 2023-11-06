from UI_primitives import *
from classes.client import *
from pymongo import *


def set_clients_block(window, db: MongoClient):
    create_label(window, "Clients", 285, 0, "s")
    temp_arr = []
    for elm in db["classes_db"]["clients"].find():
        new_class = client(def_id=elm["_id"], full_name_input=elm["fullname"], point_name_input=elm["point_name"],
                           service=elm["service_id"], phone_num_input=elm["phone_num"])
        temp_arr.append(new_class)

    create_scroll_list(window, temp_arr, 345, 50, client.get_fname)
    create_button(window, exit, 5, "Calibri", "+", 345, 230)
    create_button(window, exit, 5, "Calibri", "-", 420, 230)
    create_button(window, exit, 5, "Calibri", "Info", 380, 270)
