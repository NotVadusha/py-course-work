from UI_primitives import *
from classes.master import master
from pymongo import *
from views.create_master_window import *
from views.class_info_window import *


def set_masters_block(window: Frame, refresh, db: MongoClient):
    create_label(window, "Masters", 0, 0, "s")
    temp_arr = []
    for elm in db["classes_db"]["masters"].find():
        new_class = master(def_id=elm["_id"], full_name_input=elm["fullname"], point_name_input=elm["point_name"],
                           address_input=elm["address"], phone_num_input=elm["phone_num"],
                           specialization_input=elm["specialization"])
        temp_arr.append(new_class)
    masters_listbox = create_scroll_list(window, temp_arr, 50, 50, master.get_fname)

    def on_plus_click():
        create_master_window(refresh, db)

    def on_minus_click():
        position_set = masters_listbox.curselection()
        if position_set:
            position = position_set[0]
            master_to_delete = temp_arr[position]
            db["classes_db"]["masters"].delete_one({"_id": master_to_delete.get_id()})
            window.update()
        refresh()

    def on_show_info_click():
        position_set = masters_listbox.curselection()
        if position_set:
            position = position_set[0]
            master_to_show = temp_arr[position]
            show_obj_info_window(master_to_show)

    create_button(window, on_plus_click, 5, "Calibri", "+", 50, 230)
    create_button(window, on_minus_click, 5, "Calibri", "-", 123, 230)
    create_button(window, on_show_info_click, 5, "Calibri", "Info", 85, 270)
