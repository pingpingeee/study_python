score1 = int(input("필기시험 점수 입력 : "))
score2 = int(input("실기시험 점수 입력 : "))
line = 80
yn = "불합격"

if score1 >= line and score2 >= line:
    yn="합격"

print("- 필기시험 점수 : ", score1)
print("- 실기시험 점수 : ", score2)
print("- 판정 : ", yn)
