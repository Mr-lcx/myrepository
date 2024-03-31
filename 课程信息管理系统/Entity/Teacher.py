
"""
    教师类
"""
from Entity.Person import Person


class Teacher(Person):
    def __init__(self, id, name,sex, phone,xueyuan):
        super().__init__(id, name, sex,'teacher',xueyuan)
        self.phone = phone

    def __str__(self):
        super().__str__()
