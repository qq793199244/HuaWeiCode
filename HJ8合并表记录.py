while 1:
    try:
        n = int(input())
        dic = {}
        for _ in range(n):
            k, v = map(int, input().split())
            if k in dic:
                dic[k] += v
            else:
                dic[k] = v
        for k in sorted(dic):
            print(k, dic[k])
    except:
        break