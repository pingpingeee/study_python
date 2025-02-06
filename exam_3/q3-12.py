num = int(input("양의 정수 입력 : "))

if num % 4 == 0 and num % 3 == 0:
    print("%d은(는) 3의 배수이면서 4의 배수" % num)
elif num % 3 == 0:
    print("%d은(는) 3의 배수" % num)
elif num % 4 == 0:
    print("%d은(는) 4의 배수" % num)
else :
    print("%d은(는) 3의 배수도 4의 배수도 아니다" % num)
