# 문자열의 인덱스를 검사하는 방법
# num = input("숫자 입력 : ")

# count = 0

# for i in range(len(num)):
#     if int(num[i]) % 2 != 0:
#         count += 1

# print("홀수 개수 : %d" % count)

c = 0
num2 = input("숫자 입력 : ")
for a in num2:  # a안에 num2를 넣음
    a = int(a)  # 정수변환

    if a % 2 == 1:
        c += 1
print("홀수 개수 : %d" % c)
