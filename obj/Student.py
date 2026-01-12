import math
import time


class Student:

    def __init__(self, name, age):
        self.__name = name
        self._age = age

    def study(self, course_name):
        print(f'学生{self.__name}正在学习{course_name}.')

    def play(self):
        print(f'{self.__name}正在玩游戏.')


class Clock:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def run(self):
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
            if self.minute == 60:
                self.minute = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0

    def show(self):
        return f'{self.hour:0>2d}:{self.minute:0>2d}:{self.second:0>2d}'

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def add_x_y(self):
        return self.x + self.y

    def distance_to(self, other:Point) -> float:
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx * dx + dy * dy)

    @staticmethod
    def is_valid(a:int, b:int, c:int):
        return a + b > c and a + c > b and b + c > a

    @classmethod
    def is_valid2(cls, a:int, b:int, c:int):
        return a + b > c and a + c > b and b + c > a


if __name__ == '__main__':
    stu1 = Student('wm', 11)
    # print(stu1._age)
    # print(stu1.__name)
    # 私有属性也能访问
    # print(stu1._Student__name)
    # stu2 = Student('hl', 13)
    # print(stu1)
    # print(stu2)
    # print(id(stu1))
    # print(hex(id(stu2)))
    # stu1.study('Vue')
    # stu2.play()

    # clock = Clock()
    # while True:
    #     print(clock.show())
    #     time.sleep(1)
    #     clock.run()

    p1 = Point(200, 200)
    p2 = Point(400, 400)
    f:float = p1.distance_to(p2)
    print(f'distance: {f:.2f}')

    print(Point.is_valid(1, 2, 3))
    Point.is_valid2(1,2, 3)
    print(p1.add_x_y)