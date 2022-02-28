def func(n):
    res = 0
    while n != 0:
        if n % 2 == 1:
            res += 1
        n = n >> 1
    return res


while 1:
    try:
        n = int(input())
        print(func(n))
    except:
        break
