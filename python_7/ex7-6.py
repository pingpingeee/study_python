def cir_area():
    result = r * r * 3.14
    return result


def cir_length():
    result = 2 * 3.14 * r
    return result


r = int(input("반지름 입력 : "))
area = cir_area()
length = cir_length()
print("원의 면적 : %.1f, 원주의 길이 : %.1f" % (area, length))
