class Person:
    def __init__(self, age):
        self.__age = 1
        self.age = age

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, v):
        if v > 0:
            self.__age = v


kolya = Person(-20)

print(kolya.age)
