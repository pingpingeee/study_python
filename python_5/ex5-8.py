scores = []

while True:
    # 50, 60, 70, -1 입력
    score = int(input("성적 입력 (종료 : -1): "))
    if score == -1:
        break

    scores.append(score)

print(scores)  # [50, 60, 70] 출력
