"""
주석기능
"""
name = input("당신의 이름은?")
birth = int(input("당신의 태어난 해는?"))

age = 2025 - birth

print("%s님의 나이는 %d세 입니다." % (name, age))
