price = 3000
num = 3
pay = 10000

change = pay - price * num

# print(change)
# print("거스름돈 -->" change) # 오류
# print("거스름돈 --> 원" % change)  # 오류
# print("거스름돈 --> %d원" % change)  # change변수를 정수형태 %d로 받음
print("거스름돈 --> %f원" % change)  # change변수를 실수형태 %f로 받음