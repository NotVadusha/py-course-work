import uuid


class service:
    def __init__(self, service_type_input, service_name, service_cost, service_appointed_to, def_id=uuid.uuid4()):
        self.id = def_id
        self.service_type = service_type_input
        self.name = service_name
        self.cost = service_cost
        self.appointed_to = service_appointed_to

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def to_dict(self):
        return {
            "_id": self.id,
            "service_type": self.service_type,
            "service_name": self.name,
            "service_cost": self.cost,
            "service_appointed_to": self.appointed_to,
        }
