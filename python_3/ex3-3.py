# 조건문 기초
score = int(input("점수입력 : "))

if score >= 90:
    grade = "A"
    print("등급 : ", grade)
elif score >= 80:
    grade = "B"
    print("등급 : ", grade)
elif score >= 70:
    grade = "C"
    print("등급 : ", grade)
elif score >= 60:
    grade = "D"
    print("등급 : ", grade)
else:
    grade = "F"
    print("등급 : ", grade)
