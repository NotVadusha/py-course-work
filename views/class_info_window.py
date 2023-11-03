from classes.service import *
from classes.master import *
from classes.client import *
from UI_primitives import *


def show_obj_info_window(obj: service | client | master):
    info_window = create_new_window("500x500")
    object_props = obj.to_dict()

    x = 10
    y = 50
    i=0
    abc = []
    abc.append(create_label(info_window, {object_props.keys()[0]}, x, y, 's'))

    for prop in object_props.keys():
        print(prop, i)
        i+=1
        x += 50
        print(x)
    return obj.to_dict()


