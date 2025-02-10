def show():
    print("- 선택옵션")
    print("1. 더하기")
    print("2. 빼기")
    print("3. 곱하기")
    print("4. 나누기")


def cal(n, num1, num2):
    global g
    if n == "1":
        g = "+"
        return num1 + num2
    elif n == "2":
        g = "-"
        return num1 - num2
    elif n == "3":
        g = "*"
        return num1 * num2
    elif n == "4":
        g = "/"
        return num1 / num2


show()
n = input("원하는 연산 선택 (1/2/3/4)")
num1 = int(input("첫 번째 숫자 입력 : "))
num2 = int(input("두 번째 숫자 입력 : "))
result = cal(n, num1, num2)

print("%d %s %d = %d" % (num1, g, num2, result))
