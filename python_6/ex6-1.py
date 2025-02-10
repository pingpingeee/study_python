animals = ("토끼", "거북이", "사자", "여우")
print(animals)


# 오류발생 튜플이라 값 변경불가
# animals[2] = "호랑이"
# print(animals)

# num = tuple(range(10))
# print(num)
num = tuple(range(10, 21))
print(num)

print("num[0] : ", num[0])
print("num[2:5] : ", num[2:5])  # 인덱스 2 ~ 4
print("num[2] : ", num[2])
print("num[:5] : ", num[:5])  # 인덱스 4까지
print("num[-2] : ", num[-2])  # 인덱스 맨뒤에서 두번째
print("num[::-1] : ", num[::-1])  # ::-1 => 맨뒤에서 맨앞으로 출력
