def func(str, search):
    count = 0
    for i in range(len(str)):
        if str[i] == search:
            count += 1
    return count


str = input("영어 문장 입력 : ")
search = input("알파벳 하나 입력 : ")
co = int(func(str, search))

print("%s에 포함된 %s의 개수는 %d이다." % (str, search, co))