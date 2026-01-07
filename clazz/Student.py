class Student:

    def __init__(self, name, age):
        """初始化"""
        self.name = name
        self.age = age

    def study(self, course_name):
        print(f'学生{self.name}正在学习{course_name}')


if __name__ == '__main__':
    student = Student(name='gf', age=20)
    student.study('math')
    print(hex(id(student)))