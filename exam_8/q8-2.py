class Cla:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def cal(self):
        self.result = (self.x + self.y) / 2 * self.z

    def show(self):
        print("사다리꼴의 면적 : %.2f" % self.result)


num1 = int(input("사다리꼴 밑변의 길이 입력 : "))
num2 = int(input("윗변의 길이 입력 : "))
num3 = int(input("높이 입력 : "))

result = Cla(num1, num2, num3)
result.cal()
result.show()
