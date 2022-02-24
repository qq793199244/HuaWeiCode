def func(s):
    dic = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    res = 0
    num = s[2:]
    length = len(num)
    for i in range(length):
        if num[i] in dic:
            res += dic[num[i]] * 16 ** (length - 1 - i)
        else:
            res += int(num[i]) * 16 ** (length - 1 - i)
    return res


while 1:
    try:
        n = str(input())
        print(func(n))
    except:
        break
