import tkinter
from tkinter import *
from tkinter import ttk
import tkinter.messagebox


def create_label(window, text, x, y, anch):
    label = Label(window, text=text, bg='#C1C1C1', font='Arial 12', anchor=anch, fg='#000000', width=25)
    label.pack()
    label.place(x=x, y=y)
    return label


def create_scroll_list(window, arr, x, y, elm_method):
    listbox = Listbox(window, bg='Gray')
    for element in arr:
        listbox.insert(END, elm_method(element))
    listbox.pack()
    listbox.place(x=x, y=y)
    return listbox


def create_input(window, insert, x, y):
    takeinfo = Entry(window, bg='#C1C1C1', width=30)
    takeinfo.pack()
    takeinfo.insert(0, insert)
    takeinfo.place(x=x, y=y)
    return takeinfo


def create_combo(window, value, x, y, state):
    combobox = ttk.Combobox(window, values=value, state=state)
    combobox.pack(anchor='s', fill=X)
    combobox.set(value[0])
    combobox.place(x=x, y=y)
    return combobox


def create_new_window(geometry):
    top_lvl = Toplevel()
    top_lvl.title("Пункт ксерокопії")
    top_lvl.geometry(geometry)
    top_lvl.resizable(width=False, height=False)
    top_lvl.configure(bg='#C1C1C1')
    return top_lvl


def create_button(window, command, width, font, text, x, y):
    created_button = Button(window,
                            text=text,
                            bg='#C1C1C1',
                            command=command,
                            font=font,
                            width=width,
                            activebackground='#FFFFFF'
                            )
    created_button.pack()
    created_button.place(x=x, y=y)
    return created_button
