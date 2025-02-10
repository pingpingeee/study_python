temp = {
    "월": 15.5,
    "화": 17.0,
    "수": 16.2,
    "목": 12.9,
    "금": 11.0,
    "토": 10.5,
    "일": 13.3,
}

min = temp["월"]

for i in temp:
    if temp[i] < min:
        min = temp[i]
        day = i

print("요일 : %s, 최저기온 : %.1f" % (day, min))