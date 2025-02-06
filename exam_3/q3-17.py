print("기능선택")
print("1. 더하기")
print("2. 빼기")
print("3. 곱하기")
print("4. 나누기")

cal = input("계산기 기능 선택 ( 1 / 2 / 3 / 4 ) : ")
num1 = int(input("첫 번째 숫자 입력 : "))
num2 = int(input("두 번째 숫자 입력 : "))

if cal == '1':
    print("%d + %d = %d" % (num1, num2, num1 + num2))
elif cal == '2':
    print("%d - %d = %d" % (num1, num2, num1 - num2))
elif cal == '3':
    print("%d * %d = %d" % (num1, num2, num1 * num2))
elif cal == '4':
    print("%d / %d = %d" % (num1, num2, num1 / num2))
else:
    print("잘못된 연산 입력")