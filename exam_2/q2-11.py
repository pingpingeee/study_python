y = input("년은?")
m = input("월은?")
d = input("일은?")

#join
result = ".".join([y, m, d])

print("join() => ", result)

# sep 활용
print("sep= =>", y, m, d, sep=".")
