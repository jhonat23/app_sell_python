import uuid


class Client():
    def __init__(self, name, company, email, position, uid=None):
        self.name = name
        self.company = company
        self.email = email
        self.position = position
        self.uid = uid or uuid.uuid4() #'or' choices only by bool(val)=True
    
    def to_dict(self):
        return vars(self)

    @staticmethod#method can be executed without an instance
    def schema():
        return ['name', 'company', 'email', 'position', 'uid']

if __name__ == '__main__':
    print(dir(Client))