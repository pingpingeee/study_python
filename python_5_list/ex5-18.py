data = [12, 8, 15, 32, -3, -20, 15, 34, 6]
print(data)

# sort() => 오름차순 정렬
data.sort()
print(data)  # [-20, -3, 6, 8, 12, 15, 15, 32, 34] 출력

# sort(reverse+True) => 내림차순 정렬렬
data.sort(reverse=True)
print(data)  # [34, 32, 15, 15, 12, 8, 6, -3, -20] 출력
