i = 0
count = 0

while i <= 1000:
    if i % 3 != 0:
        print(i, end=" ")
        count += 1
    if count == 0:
        count = 1
        print("")
    i += 1
