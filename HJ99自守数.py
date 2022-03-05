def func(n):
    res = 0
    for i in range(n + 1):
        if str(i) == str(i ** 2)[-len(str(i)):]:
            res += 1
    return res


while 1:
    try:
        n = int(input())
        print(func(n))
    except:
        break
