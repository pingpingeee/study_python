class Person:
    def __init__(self, name):
        self.name = name

    def showName(self):
        print("Person showName() => ", self.name)


class Student(Person):
    def showName(self):
        print("Student showName() => ", self.name)


# x = Student()  # 오류
x = Student("홍길동")
x.showName()
