
# @explain
"""
    管理员类
"""
from Entity.Person import Person


class Admin(Person):
    def __init__(self, id, name, phone=None):
        super().__init__(id, name, "",'admin', phone)  # TODO 与父类传参不一致

    def __str__(self):
        return super().__str__()
