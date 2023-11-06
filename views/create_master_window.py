import tkinter
import tkinter.messagebox

from classes.master import *
from UI_primitives import *
from pymongo import *


def create_master_window(refresh, mongo: MongoClient):
    created_window = create_new_window("400x500")
    masters = mongo["classes_db"]["masters"]

    x = 75
    y = 50
    create_label(created_window, "Create new master", x, y-30, 's')
    create_label(created_window, "Full name", x, y, 's')
    name_inp = create_input(created_window, "Oleksiy Serhiy Danylo", x+27, y+30)

    create_label(created_window, "Point name", x, y+60, 's')
    point_inp = create_input(created_window, "Place №4", x+27, y+90)

    create_label(created_window, "Address", x, y+120, 's')
    address_inp = create_input(created_window, "Based street", x+27, y+150)

    create_label(created_window, "Phone num", x, y+180, 's')
    phone_inp = create_input(created_window, "+38", x+27, y+210)

    create_label(created_window, "Specialization", x, y+240, 's')
    specs_inp = create_input(created_window, "Color prints", x+27, y+270)

    def create_object():
        if name_inp.get() == "":
            tkinter.messagebox.showerror("Пункт ксерокопії", "Name field is empty")
        if point_inp.get() == "":
            tkinter.messagebox.showerror("Пункт ксерокопії", "Point name field is empty")
        if address_inp.get() == "":
            tkinter.messagebox.showerror("Пункт ксерокопії", "Address field is empty")
        if phone_inp.get() == "":
            tkinter.messagebox.showerror("Пункт ксерокопії", "Phone field is empty")
        if specs_inp.get() == "":
            tkinter.messagebox.showerror("Пункт ксерокопії", "Specialization field is empty")

        try:
            name = name_inp.get()
            point = point_inp.get()
            address = address_inp.get()
            phone = phone_inp.get()
            specs = specs_inp.get()
            masters.insert_one(master(full_name_input=name, point_name_input=point,
                                      address_input=address, phone_num_input=phone,
                                      specialization_input=specs).to_dict())
            created_window.destroy()
            refresh()
        except Exception as e:
            tkinter.messagebox.showerror("Пункт ксерокопії", str(e))

    create_button(created_window, create_object, 10, "Calibri", "Create", x+72, y+320)
    create_button(created_window, created_window.destroy, 5, "Calibri", "Exit", x+94, y+370)
