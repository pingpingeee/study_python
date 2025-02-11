def average(*args):
    # print(args)  # 여러개의 값 출력이 튜플형식
    num_args = len(args)
    sum = 0

    for i in range(num_args):
        sum += args[i]

    avg = sum / num_args
    print("%d개 과목의 평균 : %.1f" % (num_args, avg))


average(85, 96, 87)
