name = input("당신의 이름은?")
birth = int(input("당신의 태어난 해는?"))  # 숫자를 입력해도 문자로 받음 int()를 통해 정수형으로 변환

age = 2025 - birth # 정수에서 문자열을 빼기에 오류


# print("%s님" % name)
# print("%s님 %s" % (name, birth))
print("%s님의 나이는 %d세 입니다." % (name, age))
