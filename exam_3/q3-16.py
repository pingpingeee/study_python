num1 = int(input("첫 번째 숫자 입력 : "))
num2 = int(input("두 번째 숫자 입력 : "))
cal = input("원하는 연산 입력(+, -, *, /) : ")

if cal == "+":
    print("%d + %d = %d" % (num1, num2, num1 + num2))
elif cal == '-':
    print("%d - %d = %d" % (num1, num2, num1 - num2))
elif cal == '*':
    print("%d x %d = %d" % (num1, num2, num1 * num2))
elif cal == '/':
    print("%d / %d = %d" % (num1, num2, num1 / num2))
else:
    print("잘못된 연산 입력")