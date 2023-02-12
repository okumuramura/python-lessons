class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return f'{self.name} {self.age} yo'

class Student(Person):
    def study(self):
        print(f'{self.name} is studying...')

