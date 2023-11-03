from UI_primitives import *
from classes.service import *


def set_services_block(window, db):
    create_label(window, "Services", 570, 0, "s")
    temp_arr = []
    for elm in db.find():
        new_class = service(def_id=elm["_id"], service_type_input=elm["service_type"], service_cost=elm["service_cost"],
                            service_name=elm["service_name"], service_appointed_to=elm["service_appointed_to"])
        temp_arr.append(new_class)

    create_scroll_list(window, temp_arr, 625, 50, service.get_name)
    create_button(window, exit, 5, "Calibri", "+", 625, 230)
    create_button(window, exit, 5, "Calibri", "-", 700, 230)
    create_button(window, exit, 5, "Calibri", "Info", 665, 270)
