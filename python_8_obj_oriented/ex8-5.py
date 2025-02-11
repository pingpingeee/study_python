class Student:
    pet = []

    def __init__(self):
        self.pet = []

    def push_pet(self, x):
        self.pet.append(x)


john = Student()
john.push_pet("고양이")
print(john.pet)

asdf = Student()
asdf.push_pet("강아지")
# print(asdf.pet)  # 클래스속성이라 객체들 공유됨
print(asdf.pet)  # 객체 속성이라 공유되지않음
