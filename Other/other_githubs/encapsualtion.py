# Encapsulation

class Student:

    def __init__(self):
        self.name = ""
        self.age = 0
        self.group = ""
        self.game = "pc games"

    def getAttributes(self):
        print("Student {}, {} years old is a member of {} and playes {}" .format(self.name,
                                                                                 self.age,
                                                                                 self.group,
                                                                                 self.game))



ivan = Student()
ivan.name = "Ivan"
ivan.age = 23
ivan.group = "chess players group"