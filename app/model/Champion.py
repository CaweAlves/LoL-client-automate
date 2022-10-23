class Champion:

    def __init__(self, name, role):
        self.name = name
        self.role = role

    def get_name(self):
        return self.name

    def get_role(self):
        return self.role
    
    def set_name(self, name):
        self.name = name

    def set_role(self, role):
        self.role = role