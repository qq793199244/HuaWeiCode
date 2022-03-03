def func(s):
    dic = {}
    res = ''
    for c in s:
        dic[c] = dic.get(c, 0) + 1
    tmp = sorted(dic.items())
    tmp = sorted(tmp, key=lambda x: x[1], reverse=True)
    for i in tmp:
        res += i[0]
    return res


while 1:
    try:
        s = str(input())
        print(func(s))
    except:
        break
