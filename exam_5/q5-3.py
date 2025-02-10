num = [7, 9, 15, 18, 30, -3, 7, 12, -16, -12]
result = 0

# sum() 사용
print("sum() => ", sum(num))

for i in range(len(num)):
    result += num[i]

print("합계 : ", result)
