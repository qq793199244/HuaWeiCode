def func(s, k):
    n = len(s)
    if k < n:
        return s[:k]
    else:
        return s


while 1:
    try:
        s = str(input())
        k = int(input())
        print(func(s, k))
    except:
        break