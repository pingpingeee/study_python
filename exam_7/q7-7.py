def func(n):
    result = []

    for i in range(int(n)):
        result.append((i+1) * (i+1))
    
    return result
    

num = int(input("n 값 입력 : "))

print(func(num))

