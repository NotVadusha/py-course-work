import tkinter.messagebox
from tkcalendar import Calendar

from classes.service import *
from UI_primitives import *
from pymongo import *


def create_service_window(refresh, mongo: MongoClient):
    created_window = create_new_window("400x600")
    services = mongo["classes_db"]["services"]

    x = 75
    y = 50
    create_label(created_window, "Create new service", x, y-30, 's')
    create_label(created_window, "Name", x, y, 's')
    name_inp = create_input(created_window, "Derek photo copy", x+27, y+30)

    create_label(created_window, "Type", x, y+60, 's')
    type_inp = create_input(created_window, "Photo copy", x+27, y+90)

    create_label(created_window, "Cost (only numbers)", x, y+120, 's')
    cost_predefined = IntVar()
    cost_inp = Entry(created_window, bg='#C1C1C1', width=30, textvariable=cost_predefined)
    cost_inp.pack()
    cost_inp.place(x=x+27, y=y+150)

    create_label(created_window, "Appointed to", x, y+180, 's')
    cal = Calendar(created_window, selectmode='day', year=2020, month=5, day=22)
    cal.pack()
    cal.place(x=x-10, y=y+210)

    def create_object():
        if name_inp.get() == "":
            tkinter.messagebox.showerror("Пункт ксерокопії", "Name field is empty")
            return
        if type_inp.get() == "":
            tkinter.messagebox.showerror("Пункт ксерокопії", "Type field is empty")
            return
        if cost_inp.get() == "":
            tkinter.messagebox.showerror("Пункт ксерокопії", "Cost field is empty")
            return
        if cal.get_date() == "":
            tkinter.messagebox.showerror("Пункт ксерокопії", "Calendar field is empty")
            return
        if services.find({"service_name": name_inp}):
            tkinter.messagebox.showerror("Пункт ксерокопії", "This name exists")
            return

        try:
            name = name_inp.get()
            serv_type = type_inp.get()
            cost = float(cost_inp.get())
            date = cal.get_date()
            services.insert_one(service(service_type_input=serv_type, service_name=name,
                                        service_cost=cost, service_appointed_to=date).to_dict())
            created_window.destroy()
            refresh()
        except TypeError:
            tkinter.messagebox.showerror("Пункт ксерокопії", "Input cost as a number")
        except Exception as e:
            tkinter.messagebox.showerror("Пункт ксерокопії", str(e))

    create_button(created_window, create_object, 10, "Calibri", "Create", x+72, y+410)
    create_button(created_window, created_window.destroy, 5, "Calibri", "Exit", x+94, y+460)
