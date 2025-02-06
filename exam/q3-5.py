num1 = int(input("첫 번째 정수 : "))
num2 = int(input("두 번째 정수 : "))
num3 = int(input("세 번째 정수 : "))

numArr = [num1, num2, num3]


if num1 > num2 and num1 > num3:
    print("%d, %d, %d 중에서 가장 큰 수는 %d입니다." % (num1, num2, num3, num1))
elif num2 > num1 and num2 > num3:
    print("%d, %d, %d 중에서 가장 큰 수는 %d입니다." % (num1, num2, num3, num2))
else:
    print("%d, %d, %d 중에서 가장 큰 수는 %d입니다." % (num1, num2, num3, num3))

# max함수 사용
# print("%d, %d, %d 중에서 가장 큰 수는 %d입니다." % (num1, num2, num3, max(numArr)))