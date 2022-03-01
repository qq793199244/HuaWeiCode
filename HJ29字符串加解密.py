def func(s, p):
    L1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    L2 = "BCDEFGHIJKLMNOPQRSTUVWXYZAbcdefghijklmnopqrstuvwxyza1234567890"
    res = ''
    if p == 1:
        for i in s:
            res += L2[L1.index(i)]
    elif p == -1:
        for i in s:
            res += L1[L2.index(i)]
    return res


while 1:
    try:
        print(func(str(input()), 1))
        print(func(str(input()), -1))
    except:
        break
