# Question 25
# Level 1
# Question:
# Define a class, which have a class parameter and have a same instance parameter.
#
# Hints:
#    Define a instance parameter, need add it in __init__ method
#    You can init a object with construct parameter or set the value later


class Dog(object):
    nickname = "KaiPai"  # class parametar

    def __init__(self, name):
        self.name = name

    def nameOfDog(self):
        print(self.name)

    def bark(self, instane_parametar):  # instance parametar
        print(instane_parametar)


name = "Kai"
myDog = Dog(name)
myDog.nameOfDog()
myDog.bark('Woof!')  # instance parametar
print(myDog.nickname)  # class parametar
