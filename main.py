import os
import tkinter.messagebox
from tkcalendar import Calendar
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
from views.services_list import *
from views.clients_list import *
from views.masters_list import *


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
set_services_block(mainWindow)
cal = Calendar(mainWindow, selectmode='day', year=2020, month=5, day=22, x=100, y=100)
cal.pack()


def get_most_expensive_service(x):
    tkinter.messagebox.showinfo("abc", x)


def get_clients_for_date():
    tkinter.messagebox.showinfo("abc", "ABC")


def get_average_service_cost():
    tkinter.messagebox.showinfo("abc", "ABC")


create_button(mainWindow, lambda x=1: get_most_expensive_service(x), 25, "Calibri", "Get clients for selected date", 10, 450)
create_button(mainWindow, get_most_expensive_service, 25, "Calibri", "Get most expensive service", 300, 450)
create_button(mainWindow, get_average_service_cost, 20, "Calibri", "Get average service cost", 600, 450)

mainWindow.mainloop()
