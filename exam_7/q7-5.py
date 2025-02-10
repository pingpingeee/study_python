def useWhile(str):
    result = ""
    index = len(str)

    while index > 0:
        result += str[index - 1]
        index -= 1
    return result


str = input("문자열 입력 : ")
print(useWhile(str))
