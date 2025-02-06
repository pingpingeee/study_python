h1 = int(input("윗변의 길이는?"))
h2 = int(input("밑변의 길이는?"))
h3 = int(input("높이는?"))

result = (h1+h2) * h3 / 2

# format 사용법
asdf = "{:.1f}".format(result)

print(asdf)
print("-사다리꼴의 면적 : %.1f" % (result))