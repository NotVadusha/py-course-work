from UI_primitives import *
from classes.service import *


def set_services_block(window):
    create_label(window, "Services", 570, 0, "s")
    services_list = [service("11", "12", "13", "14", "15"), service("21", "22", "23", "24", "25")]
    create_scroll_list(window, services_list, 625, 50, service.get_id)
    create_button(window, exit, 5, "Calibri", "+", 625, 230)
    create_button(window, exit, 5, "Calibri", "-", 700, 230)
    create_button(window, exit, 5, "Calibri", "Info", 665, 270)
