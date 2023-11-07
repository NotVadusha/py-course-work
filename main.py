import os
from dotenv import load_dotenv
from views.services_list import *
from views.clients_list import *
from views.masters_list import *
from views.class_info_window import show_obj_info_window
from views.create_client_window import *
from views.create_service_window import *
from views.clients_for_date_list import show_clients_for_date


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
        date = cal.get_date()
        services_date_query = {"service_appointed_to": date}
        services_to_date = services.find(services_date_query)
        temp_arr = []
        for service_dict in services_to_date:
            client_dict = clients.find_one({"service_id": service_dict["_id"]})
            if client_dict:
                temp_arr.append(client(full_name_input=client_dict["fullname"], point_name_input=client_dict["point_name"],
                                       phone_num_input=client_dict["phone_num"], service_id_inp=["service_id"],
                                       service_to_date=client_dict["service_date"], def_id=client_dict["_id"]))
        show_clients_for_date(temp_arr, date)

    def get_most_expensive_service():
        service_dict = services.find_one(sort=[("service_cost", -1)])
        service_to_show = service(def_id=service_dict["_id"], service_type_input=service_dict["service_type"],
                                  service_cost=service_dict["service_cost"], service_name=service_dict["service_name"], service_appointed_to=service_dict["service_appointed_to"])
        show_obj_info_window(service_to_show)

    def get_average_service_cost():
        avg_cost = db["classes_db"]["services"].aggregate([{
            '$group': {
                '_id': None,
                'avg_service_cost': {'$avg': '$service_cost'}
            }}])
        cost_arr = []
        for x in avg_cost:
            cost_arr.append(x)
        if len(cost_arr)>0:
            return cost_arr[0]["avg_service_cost"]
        else:
            return 0

    create_button(mainWindow, get_clients_for_date, 25, "Calibri", "Get clients for selected date", 30, 550)
    create_button(mainWindow, get_most_expensive_service, 25, "Calibri", "Get most expensive service", 300, 350)
    create_label(mainWindow, f"Average service cost: {get_average_service_cost()}$", 530, 350, "w")


create_main_frame()
root.mainloop()
