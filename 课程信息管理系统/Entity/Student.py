"""
学生实体类
"""
from Entity.Person import Person


class Student(Person):
    def __init__(self, id, name, sex,xueyuan,classes):
        super().__init__(id, name, sex,'student',xueyuan)
        self.classes=classes

    def __str__(self):
        return super().__str__()
