class Person:
    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, v):
        if v > 0:
            self.__age = v


kolya = Person(23)

print(kolya.age)

kolya.age = -1  # do nothing

print(kolya.age)  # 23

kolya.age = 24
print(kolya.age)  # 24
