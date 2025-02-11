# class Cla:
#     def cal(self, x, y):
#         self.x = x
#         self.y = y
#         result = (x * y) / 2
#         print("삼각형의 면적 : %.2f" % result)

# num1 = int(input("삼각형 밑변의 길이 입력 : "))
# num2 = int(input("높이 입력 : "))

# result = Cla()

# result.cal(num1, num2)


class Cla:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def cal(self):
        self.result = (self.x * self.y) / 2

    def show(self):
        print("삼각형의 면적 : %.2f" % self.result)


num1 = int(input("삼각형 밑변의 길이 입력 : "))
num2 = int(input("높이 입력 : "))

result = Cla(num1, num2)
result.cal()
result.show()
