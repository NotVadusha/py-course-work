import uuid
from classes.user import user


class master(user):
    def __init__(self, full_name_input, point_name_input, address_input, phone_num_input, specialization_input):
        super().__init__(full_name_input, point_name_input, phone_num_input)
        self.address = address_input
        self.specialization = specialization_input
