while True:
    try:
        n = int(input())
        rule = int(input())
        flag = True
        if rule == 0:
            flag = True
        if rule == 1:
            flag = False
        score_list = []
        for _ in range(n):
            k, v = map(str, input().split())
            score_list.append([k, int(v)])

        new_list = sorted(score_list, key=lambda x: x[1], reverse=flag)

        for k, v in new_list:
            print(k, v)
    except:
        break
