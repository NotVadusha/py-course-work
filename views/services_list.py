
from views.create_service_window import *
from views.class_info_window import *


def set_services_block(window: Frame, refresh,  db: MongoClient):
    create_label(window, "Services", 570, 0, "s")
    temp_arr = []
    for elm in db["classes_db"]["services"].find():
        new_class = service(def_id=elm["_id"], service_type_input=elm["service_type"], service_cost=elm["service_cost"],
                            service_name=elm["service_name"], service_appointed_to=elm["service_appointed_to"])
        temp_arr.append(new_class)

    services_listbox = create_scroll_list(window, temp_arr, 625, 50, service.get_name)

    def on_plus_click():
        create_service_window(refresh, db)

    def on_minus_click():
        position_set = services_listbox.curselection()
        if position_set:
            position = position_set[0]
            service_to_delete = temp_arr[position]
            db["classes_db"]["services"].delete_one({"_id": service_to_delete.get_id()})
            window.update()
        refresh()

    def on_show_info_click():
        position_set = services_listbox.curselection()
        if position_set:
            position = position_set[0]
            service_to_show = temp_arr[position]
            show_obj_info_window(service_to_show)

    create_button(window, on_plus_click, 5, "Calibri", "+", 625, 230)
    create_button(window, on_minus_click, 5, "Calibri", "-", 700, 230)
    create_button(window, on_show_info_click, 5, "Calibri", "Info", 665, 270)
