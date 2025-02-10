def func(n):
    m = n * 0.621371
    return m

num1 = int(input("킬로미터 입력 : "))
result = func(num1)

print("%d킬로미터는 %.2f 마일이다." % (num1, result))
