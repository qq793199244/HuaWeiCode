def func(n):
    sn = n * 2 + (n * (n - 1)) * 3 // 2
    return sn


while 1:
    try:
        n = int(input())
        print(func(n))
    except:
        break
