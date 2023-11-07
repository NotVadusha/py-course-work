from classes.user import user


class master(user):
    def __init__(self, full_name_input, point_name_input, address_input, phone_num_input, specialization_input, def_id=0):
        super().__init__(full_name_input, point_name_input, phone_num_input, def_id)
        self.address = address_input
        self.specialization = specialization_input

    def to_dict(self):
        return {
            "_id": self.id,
            "fullname": self.full_name,
            "point_name": self.point_name,
            "address": self.address,
            "phone_num": self.phone_num,
            "specialization": self.specialization,
        }

    def to_formatted_string(self):
        return f'Master:\nName: {self.full_name}\nPhone: {self.phone_num}\nPoint: {self.point_name}\nAddress: {self.address}\nSpecialization: {self.specialization}'
