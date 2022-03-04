def func(s):
    res = 0
    for c in s:
        if c >= 'A' and c <= 'Z':
            res += 1
    return res


while 1:
    try:
        s = str(input())
        print(func(s))
    except:
        break
