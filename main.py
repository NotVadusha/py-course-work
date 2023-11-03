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

mainWindow = Tk()
mainWindow.title("Пункт ксерокопії")
mainWindow.geometry("800x600")
mainWindow.resizable(width=False, height=False)
mainWindow.configure(bg='#CCCCCC')

set_masters_block(mainWindow)
set_clients_block(mainWindow)
set_services_block(mainWindow, services)
cal = Calendar(mainWindow, selectmode='day', year=2020, month=5, day=22)
cal.pack()
cal.place(x=10, y=350)


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


a = master("1", "2", "3", "4", "5")
c = service("1", "2", "3", "4")
b = client("1", "2", "3", c)

show_obj_info_window(a)
show_obj_info_window(b)
show_obj_info_window(c)
create_button(mainWindow, get_clients_for_date, 25, "Calibri", "Get clients for selected date", 30, 550)
create_button(mainWindow, get_most_expensive_service, 25, "Calibri", "Get most expensive service", 300, 450)
create_button(mainWindow, get_average_service_cost, 20, "Calibri", "Get average service cost", 600, 450)

mainWindow.mainloop()
