import tkinter
import tkinter.messagebox

from classes.client import *
from classes.service import *
from UI_primitives import *
from pymongo import *


def create_client_window(refresh, mongo: MongoClient):
    created_window = create_new_window("400x500")
    clients = mongo["classes_db"]["clients"]

    x = 75
    y = 50
    create_label(created_window, "Create new master", x, y-30, 's')
    create_label(created_window, "Full name", x, y, 's')
    name_inp = create_input(created_window, "Oleksiy Serhiy Danylo", x+27, y+30)

    create_label(created_window, "Point name", x, y+60, 's')
    point_inp = create_input(created_window, "Place №4", x+27, y+90)

    create_label(created_window, "Phone num", x, y+120, 's')
    phone_inp = create_input(created_window, "+38", x+27, y+150)

    create_label(created_window, "Pick service", x, y+180, 's')
    service_inp = create_input(created_window, "+38", x+27, y+210)

    def create_object():
        if name_inp.get() == "":
            tkinter.messagebox.showerror("Пункт ксерокопії", "Name field is empty")
        if point_inp.get() == "":
            tkinter.messagebox.showerror("Пункт ксерокопії", "Point name field is empty")
        if phone_inp.get() == "":
            tkinter.messagebox.showerror("Пункт ксерокопії", "Phone field is empty")
        if service_inp.get() == "":
            tkinter.messagebox.showerror("Пункт ксерокопії", "Service field is empty")

        try:
            name = name_inp.get()
            point = point_inp.get()
            service_id = service_inp.get()
            phone = phone_inp.get()

            clients.insert_one(client(full_name_input=name, point_name_input=point,
                                      service_id_inp=service_id, phone_num_input=phone).to_dict())
            created_window.destroy()
            refresh()
        except Exception as e:
            tkinter.messagebox.showerror("Пункт ксерокопії", str(e))

    create_button(created_window, create_object, 10, "Calibri", "Create", x+72, y+320)
    create_button(created_window, created_window.destroy, 5, "Calibri", "Exit", x+94, y+370)
