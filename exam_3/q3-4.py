num = int(input("주민번호 뒷자리 첫 번째 숫자 입력 : "))

if num == 1 or num == 3:
    print("남성")
elif num == 2 or num == 4:
    print("여성")
else:
    print("잘못된 값")