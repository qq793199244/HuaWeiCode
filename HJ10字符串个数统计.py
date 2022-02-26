def func(s):
    dic = {}
    res = 0
    for c in s:
        if c in dic:
            continue
        else:
            dic[c] = dic.get(c, 0) + 1
            res += 1
    return res


while 1:
    try:
        s = str(input())
        print(func(s))
    except:
        break
