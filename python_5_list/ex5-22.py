hello = "have a nice day"
print(hello)

# split("문자") => 해당 문자를 기준으로 분리
list1 = hello.split(" ")
print(list1)  # ['have', 'a', 'nice', 'day'] 출력

# type() => 해당 객체 타입반환
print(type(list1))  # <class 'list'> 출력

for i in range(0, len(list1)):
    print("list[%d] : %s" % (i, list1[i]))
    # 출력
    # list[0] : have
    # list[1] : a
    # list[2] : nice
    # list[3] : day
