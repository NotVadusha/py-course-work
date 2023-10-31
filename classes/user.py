import uuid


class user:
    def __init__(self, full_name_input, point_name_input, phone_num_input):
        self.id = uuid.UUID
        self.full_name = full_name_input
        self.point_name = point_name_input
        self.phone_num = phone_num_input
