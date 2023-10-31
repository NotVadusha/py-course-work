import uuid
from classes.user import user


class client(user):
    def __init__(self, full_name_input, point_name_input, phone_num_input, service):
        super().__init__(full_name_input, point_name_input, phone_num_input)
        self.service_id = service.get_id()
