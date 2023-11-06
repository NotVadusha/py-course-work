from UI_primitives import *
from classes.client import *
from pymongo import *
from views.create_client_window import *
from views.class_info_window import *


def set_clients_block(window: Frame, refresh, db: MongoClient):
    create_label(window, "Clients", 285, 0, "s")
    temp_arr = []
    for elm in db["classes_db"]["clients"].find():
        new_class = client(def_id=elm["_id"], full_name_input=elm["fullname"], point_name_input=elm["point_name"],
                           service_id_inp=elm["service_id"], phone_num_input=elm["phone_num"])
        temp_arr.append(new_class)

    clients_listbox = create_scroll_list(window, temp_arr, 345, 50, client.get_fname)

    def on_plus_click():
        create_client_window(refresh, db)

    def on_minus_click():
        position_set = clients_listbox.curselection()
        if position_set:
            position = position_set[0]
            client_to_delete = temp_arr[position]
            db["classes_db"]["clients"].delete_one({"_id": client_to_delete.get_id()})
            refresh()

    def on_show_info_click():
        position_set = clients_listbox.curselection()
        if position_set:
            position = position_set[0]
            client_to_show = temp_arr[position]
            show_obj_info_window(client_to_show)

    create_button(window, on_plus_click, 5, "Calibri", "+", 345, 230)
    create_button(window, on_minus_click, 5, "Calibri", "-", 420, 230)
    create_button(window, on_show_info_click, 5, "Calibri", "Info", 380, 270)
