grade = input("등급 입력 (A+, A, B+, ..., F): ")

if grade == "A+" or grade == "a+":
    num = float(4.5)
    print("등급 : %s, 평점 %.1f" % (grade, num))
elif grade == "A" or grade == "a":
    num = float(4)
    print("등급 : %s, 평점 %.1f" % (grade, num))
elif grade == "B+" or grade == "b+":
    num = float(3.5)
    print("등급 : %s, 평점 %.1f" % (grade, num))
elif grade == "B" or grade == "b":
    num = float(3)
    print("등급 : %s, 평점 %.1f" % (grade, num))
elif grade == "C+" or grade == "c+":
    num = float(2.5)
    print("등급 : %s, 평점 %.1f" % (grade, num))
elif grade == "C" or grade == "c":
    num = float(2)
    print("등급 : %s, 평점 %.1f" % (grade, num))
elif grade == "D+" or grade == "d+":
    num = float(1.5)
    print("등급 : %s, 평점 %.1f" % (grade, num))
elif grade == "D" or grade == "d":
    num = float(1)
    print("등급 : %s, 평점 %.1f" % (grade, num))
else:
    num = float(1)
    print("등급 : %s, 평점 %.1f미만" % (grade, num))