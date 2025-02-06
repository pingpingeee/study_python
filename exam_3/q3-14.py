num = int(input("숫자 입력 : "))

if num < 10:
    print("%d은(는) 한 자리 숫자" % num)
elif num >= 10 and num <= 1000:
    print("%d은(는) 두 자리 숫자" % num)
else:
    print("오류! %d은(는) 범위 (0 ~ 999) 이외의 숫자" % num)
