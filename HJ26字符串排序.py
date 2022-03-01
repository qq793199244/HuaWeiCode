def func(s):
    ch = ''
    for c in s:
        if c.isalpha():
            ch += c
    new_ch = sorted(ch, key=str.upper)
    res = ''
    idx = 0
    for i in range(len(s)):
        if s[i].isalpha():
            res += new_ch[idx]
            idx += 1
        else:
            res += s[i]
    return res


while 1:
    try:
        s = str(input())
        print(func(s))
    except:
        break
