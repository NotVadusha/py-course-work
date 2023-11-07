from UI_primitives import *
from classes.client import *
from classes.service import *
from views.class_info_window import show_obj_info_window


def show_clients_for_date(clients, date):
    window = create_new_window("170x300")
    create_label(window, f"Clients for {date}", -35, 0, "s")
    clients_listbox = create_scroll_list(window, clients, 22, 50, client.get_fname)

    def on_show_info_click():
        position_set = clients_listbox.curselection()
        if position_set:
            position = position_set[0]
            client_to_show = clients[position]
            show_obj_info_window(client_to_show)

    create_button(window, on_show_info_click, 5, "Calibri", "Info", 20, 230)
    create_button(window, window.destroy, 5, "Calibri", "Exit", 90, 230)
