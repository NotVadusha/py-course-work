import uuid


class user:
    def __init__(self, full_name_input, point_name_input, phone_num_input, def_id):
        self.id = def_id
        self.full_name = full_name_input
        self.point_name = point_name_input
        self.phone_num = phone_num_input

    def get_fname(self):
        return self.full_name
