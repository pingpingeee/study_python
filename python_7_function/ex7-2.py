def even_odd(n):
    if n % 2 == 0:
        print("%d은(는) 짝수" % n)
    else:
        print("%d은(는) 홀수" % n)


x = int(input("숫자 입력 : "))
even_odd(x)
