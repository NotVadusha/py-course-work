from classes.service import *
from classes.master import *
from classes.client import *
from UI_primitives import *


def show_obj_info_window(obj: service | client | master):
    info_window = create_new_window("400x300")

    obj_txt_info=obj.to_formatted_string()
    label = Label(info_window, text=obj_txt_info, font='Arial 12', fg='#000000', width=30, height=6)
    label.pack()
    label.place(x=50, y=10)

    create_button(info_window, info_window.destroy, 14, "Calibri", "Exit", 145, 200)

