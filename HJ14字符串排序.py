def func(s):
    s = sorted(s)
    return s


while 1:
    try:
        n = int(input())
        s_list = []
        for _ in range(n):
            s_list.append(str(input()))
        res = func(s_list)
        for i in range(n):
            print(res[i])
    except:
        break
