class Members:
    def __init__(self, name, age):
        pass  # 동작없이 다음 실행
        self.name = name
        self.age = age

    def show_info(self):
        print("이름 : ", self.name)
        print("나이 : ", self.age)

memeber1 = Members("홍길동", 24)
memeber1.show_info()
