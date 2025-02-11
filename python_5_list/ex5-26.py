sentences = ["aaa bb", "cc d", "e f"]

for sentence in sentences:

    x = sentence.replace(" ", "-")
    print(x)
    # 출력
    # aaa-bb
    # cc-d
    # e-f
