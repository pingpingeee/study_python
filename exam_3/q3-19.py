account = input("아이디 입력 : ")
if account == "admin":
    print("콘텐츠 이용 가능")
else:
    level = int(input("회원 레벨 입력 : "))
    if level >= 1 and level <= 3:
        print("컨텐츠 이용 가능")
    else:
        print("컨텐츠 이용 불가능")
