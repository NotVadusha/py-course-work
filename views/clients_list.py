from UI_primitives import *
from classes.client import *
from classes.service import *


def set_clients_block(window):
    create_label(window, "Masters", 0, 0, "s")

    create_label(window, "Clients", 285, 0, "s")
    clients_list = [client("11", "12", "13", "14", service("11", "12", "13", "14", "15")),
                    client("21", "22", "23", "24", service("11", "12", "13", "14", "15"))]
    create_scroll_list(window, clients_list, 345, 50, client.get_fname)
    create_button(window, exit, 5, "Calibri", "+", 345, 230)
    create_button(window, exit, 5, "Calibri", "-", 420, 230)
    create_button(window, exit, 5, "Calibri", "Info", 380, 270)
