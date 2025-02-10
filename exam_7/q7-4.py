def cal(tup):
    result = 0
    for i in range(len(tup)):
        result += tup[i]
    return int(result)

tup = (10, 20, 30, 40, 50)

print("튜플의 합계 : %d" % cal(tup))

