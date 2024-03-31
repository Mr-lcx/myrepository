"""
    所有人的基本类
"""


class Person(object):
    def __init__(self, id, name, sex, type, xueyaun):
        self.id = id
        self.name = name
        self.sex = sex
        self.type = type
        self.xueyuan = xueyaun
        self.phone = ""
        self.classes = ""

    def __str__(self):
        return 'id:[%s] name:[%s] type:[%s]' % (self.id, self.name, self.type)
