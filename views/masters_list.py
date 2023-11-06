from UI_primitives import *
from classes.master import master
from pymongo import *


def set_masters_block(window, db: MongoClient):
    create_label(window, "Masters", 0, 0, "s")
    temp_arr = []
    for elm in db["classes_db"]["masters"].find():
        new_class = master(def_id=elm["_id"], full_name_input=elm["fullname"], point_name_input=elm["point_name"],
                           address_input=elm["address"], phone_num_input=elm["phone_num"],
                           specialization_input=elm["specialization"])
        temp_arr.append(new_class)

    create_scroll_list(window, temp_arr, 50, 50, master.get_fname)
    create_button(window, exit, 5, "Calibri", "+", 50, 230)
    create_button(window, exit, 5, "Calibri", "-", 123, 230)
    create_button(window, exit, 5, "Calibri", "Info", 85, 270)
