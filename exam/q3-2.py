m = int(input("월을 숫자로 입력 : "))

if m >= 3 and m <= 5:
    print("%d은 봄" % m)
elif m >= 6 and m <= 8:
    print("%d은 여름" % m)
elif m >= 9 and m <= 11:
    print("%d은 가을" % m)
elif m == 12 or m <= 2:
    print("%d은 겨울" % m)
else:
    print("잘못된값")
