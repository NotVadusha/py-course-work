import uuid


class service:
    def __init__(self, service_type_input, service_name, service_cost, service_appointed_to):
        self.id = uuid.UUID
        self.service_type = service_type_input
        self.name = service_name
        self.cost = service_cost
        self.appointed_to = service_appointed_to

    def get_id(self):
        return self.id
