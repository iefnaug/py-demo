from enum import Enum


class Person:
    """人"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name}正在吃饭.')

    def sleep(self):
        print(f'{self.name}正在睡觉.')


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
    def eat(self):
        print(f'{self.name} : {self.age}')


class Suite(Enum):
    SPADE, HEART, CLUB, DIAMOND = range(4)

if __name__ == '__main__':
    for s in Suite:
        print(f'{s} {s.value}')
