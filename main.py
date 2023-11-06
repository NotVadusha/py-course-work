import os
import tkinter.messagebox
from tkcalendar import Calendar
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
from views.services_list import *
from views.clients_list import *
from views.masters_list import *
import datetime
from views.class_info_window import show_obj_info_window
from views.create_client_window import *
from views.create_master_window import *
from views.create_service_window import *


load_dotenv()
db = MongoClient(os.getenv("MONGO_URI"))

try:
    db.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

dblist = db.list_database_names()
if 'classes_db' in dblist:
    print('db exists')

masters = db["classes_db"]["masters"]
clients = db["classes_db"]["clients"]
services = db["classes_db"]["services"]

root = Tk()
root.title("Пункт ксерокопії")
root.geometry("800x600")
root.resizable(width=False, height=False)
root.configure(bg='#CCCCCC')


def create_main_frame():
    mainWindow = Frame(root, bg='#CCCCCC')
    mainWindow.place(relx=0, rely=0, relwidth=1, relheight=1)
    cal = Calendar(mainWindow, selectmode='day', year=2020, month=5, day=22)
    cal.pack()
    cal.place(x=10, y=350)

    def refresh_frame():
        mainWindow.destroy()
        create_main_frame()

    set_masters_block(mainWindow, refresh_frame, db)
    set_clients_block(mainWindow, refresh_frame, db)
    set_services_block(mainWindow, refresh_frame, db)

    def get_clients_for_date():
        tkinter.messagebox.showinfo("abc", cal.get_date())
        clients_via_date = []
        for client_obj in clients.find({"service_appointed_to": cal.get_date()}):
            clients_via_date.append(client(*client_obj))
        list_via_date_window = create_new_window("")
        create_scroll_list(list_via_date_window, [], 0, 0, client.get_fname)

    def get_most_expensive_service():
        tkinter.messagebox.showinfo("abc", "cal.get_date()")

    # "Right now, average service cost is " +
    def get_average_service_cost():
        x = services.aggregate(
        [{'$group': {
            "_id": "$service_name",
            'avg_cost': {'$avg': '$service_cost'}
        }}])
        print(x["avg_cost"])
        tkinter.messagebox.showinfo("Average service", "1")

    create_button(mainWindow, get_clients_for_date, 25, "Calibri", "Get clients for selected date", 30, 550)
    create_button(mainWindow, get_most_expensive_service, 25, "Calibri", "Get most expensive service", 300, 450)
    create_button(mainWindow, get_average_service_cost, 20, "Calibri", "Get average service cost", 600, 450)


create_main_frame()
root.mainloop()
