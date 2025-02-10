num = [7, 9, 15, 18, 30, -3, 7, 12, -16, -12]
numList = []
result = 0
i = 0

while i < len(num):
    if i % 2 == 1:
        numList.append(num[i])
        result += num[i]
    i += 1

print("짝수 번째 요소 : ", numList)  # 짝수 번째 요소 :  [9, 18, -3, 12, -12]
print("합계 : ", result)  # 합계 :  24
