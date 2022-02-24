def func(s):
    if len(s) <= 8:
        return s + (8 - len(s)) * '0'
    else:
        print(s[0:8])
        s = s[8:]
        return func(s)


while 1:
    try:
        s = str(input())
        print(func(s))
    except:
        break
