def func(s, c):
    n = len(s)
    s = s.lower()
    c = c.lower()
    num = 0
    for i in range(n):
        if s[i] == c:
            num += 1
    return num


while 1:
    try:
        s = str(input())
        c = str(input())
        print(func(s, c))
    except:
        break
