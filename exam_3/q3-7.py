txt = input("영문 대문자 또는 소문자를 하나 입력 : ").lower()

if txt == "a" or txt == "e" or txt == "i" or txt == "o" or txt == "u":
    print(txt, "=> 모음")
else:
    print(txt, "=> 자음")
