import uuid
from classes.user import user


class client(user):
    def __init__(self, full_name_input, point_name_input, phone_num_input, service, def_id=uuid.uuid4()):
        super().__init__(full_name_input, point_name_input, phone_num_input, def_id)
        self.service_id = service.get_id()

    def to_dict(self):
        return {
            "_id": self.id,
            "fullname": self.full_name,
            "point_name": self.point_name,
            "phone_num": self.phone_num,
            "service_id": self.service_id,
        }

    def to_formatted_string(self):
        return f'Client:\
            \nName: {self.full_name}\
            \nPhone: {self.phone_num}\
            \nPoint: $ {self.point_name}\
            \nService ID: {self.service_id}'
