def func(s):
    res = ''
    if '0' <= s[0] <= '9':
        res = '*' + s[0]
    else:
        res += s[0]
    for cur in range(1, len(s)):
        if '0' <= s[cur] <= '9':
            if '0' <= s[cur - 1] <= '9':
                res += s[cur]
            else:
                res = res + '*' + s[cur]
        else:
            if '0' <= s[cur - 1] <= '9':
                res = res + '*' + s[cur]
            else:
                res += s[cur]
    if '0' <= s[-1] <= '9':
        res += '*'
    return res


while 1:
    try:
        s = str(input())
        print(func(s))
    except:
        break
