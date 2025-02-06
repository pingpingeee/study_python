num1 = int(input("첫 번째 숫자 입력 : "))
num2 = int(input("두 번째 숫자 입력 : "))
result = num1+num2

if result % 3 == 0:
    print("%d은(는) 3의 배수이다" % result)
else:
    print("%d은(는) 3의 배수가 아니다" % result)