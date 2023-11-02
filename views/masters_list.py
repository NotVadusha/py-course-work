from UI_primitives import *
from classes.master import master


def set_masters_block(window):
    create_label(window, "Masters", 0, 0, "s")

    masters_list = [master("11", "12", "13", "14", "15"), master("21", "22", "23", "24", "25")]
    create_scroll_list(window, masters_list, 50, 50, master.get_fname)
    create_button(window, exit, 5, "Calibri", "+", 50, 230)
    create_button(window, exit, 5, "Calibri", "-", 123, 230)
    create_button(window, exit, 5, "Calibri", "Info", 85, 270)
