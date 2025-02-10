# def func(n):  # 리턴 값이 없을 때 None
def func():
    # x = n + 5
    # return x
    global x
    x = 100  # 지역변수 : 함수 내에서만 사용 가능
    print("func() : ", x)


# a = func(10)
# print(a)

# b = func(20)
# print(b)

func()
x = 200

func()
print(x)
