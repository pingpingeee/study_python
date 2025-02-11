class Members:
    total = 0

    def __init__(self, name, tel):
        self.name = name
        self.tel = tel
        Members.total += 1

    def showInfo(self):
        print("이름 : %s, 전화번호" % self.name, self.tel)


m1 = Members("홍길동", "010-1111-1111")
m2 = Members("홍길길", "010-2222-2222")
m3 = Members("홍동동", "010-3333-3333")
m1.showInfo()
m2.showInfo()
m3.showInfo()

print("총 회원수 : ", Members.total)