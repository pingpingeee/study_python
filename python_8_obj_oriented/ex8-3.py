class Members:
    def set_info(self, name):
        self.name = name
        print(name)

    def show_info(self):
        print("이름 : ", self.name)


memeber1 = Members()
memeber1.set_info("홍지수")
memeber1.show_info()

memeber2 = Members()
memeber2.set_info("홍길동")
memeber2.show_info()
