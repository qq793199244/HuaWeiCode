def func(num):
    dic = {}
    s = str(num)
    s = s[::-1]
    new_num = ''
    for c in s:
        if c in dic:
            continue
        else:
            dic[c] = dic.get(c, 0) + 1
            new_num += c
    return int(new_num)


while 1:
    try:
        num = int(input())
        print(func(num))
    except:
        break