data=[10,20,30,40,50,60,70,80]
print(data)

# pop() => 마지막 인덱스 추출
x=data.pop()
print(x) # 80 출력
print(data) # [10, 20, 30, 40, 50, 60, 70] 출력

# pop() => 값들어가면 해당 인덱스 추출
y=data.pop(2)
print(y) # 30 출력
print(data) # [10, 20, 40, 50, 60, 70]