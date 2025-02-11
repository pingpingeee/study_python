p_list1 = ["010-1111-1111", "010-2222-2222", "010-3333-3333"]
print(p_list1)

p_list2 = []
for number in p_list1:
    # x에 p_list1의 "-"을 지움
    x = number.replace("-", "")
    # p_list2에 x값을 추가
    p_list2.append(x)

print(p_list2) # ['01011111111', '01022222222', '01033333333'] 출력
