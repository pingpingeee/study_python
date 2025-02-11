class Person:
    def __init__(self, name):
        self.name = name

    def showName(self):
        print(self.name)

    def showAge(self):
        print(self.age)


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name)  # super() 부모클래스에 생성자 호출
        self.age = age

# x = Student()  # 오류
x = Student("홍길동", 24)
x.showName()
x.showAge()
