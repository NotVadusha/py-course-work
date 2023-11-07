import uuid


class service:
    def __init__(self, service_type_input, service_name, service_cost, service_appointed_to, def_id="0"):
        if def_id != "0":
            self.id = def_id
        else:
            self.id = uuid.uuid4()
        self.service_type = service_type_input
        self.name = service_name
        self.cost = service_cost
        self.appointed_to = service_appointed_to

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_date(self):
        return self.appointed_to

    def to_dict(self):
        return {
            "_id": self.id,
            "service_type": self.service_type,
            "service_name": self.name,
            "service_cost": self.cost,
            "service_appointed_to": self.appointed_to,
        }

    def to_formatted_string(self):
        return f'Service:\nName: {self.name} \nType: {self.service_type} \nCost: $ {self.cost}\nDate: {self.appointed_to}'

