start = int(input("시작 수 입력 : "))
end = int(input("끝 수 입력 : "))
num = int(input("정수 입력 : "))

if num > start and num < end:
    print("%d은(는) %d ~ %d 사이에 있다. " % (num, start, end))
else:
    print("%d은(는) %d ~ %d 사이에 없다. " % (num, start, end))
