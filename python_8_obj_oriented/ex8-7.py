class Person:
    def __init__(self, name):
        self.name = name

    def showName(self):
        print(self.name)


# Person 클래스(부모)를 상속받는 Student클래스(자식)
class Student(Person):
    pass


# x = Student()  # 오류
x = Student("홍길동")
x.showName()
