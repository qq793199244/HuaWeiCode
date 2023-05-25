def func(s):
    if len(s) <= 8:
        return 'NG'
    lower, upper, num, others = 0, 0, 0, 0
    for c in s:
        if ord('a') <= ord(c) <= ord('z'):
            lower = 1
        elif ord('A') <= ord(c) <= ord('Z'):
            upper = 1
        elif ord('0') <= ord(c) <= ord('9'):
            num = 1
        else:
            others = 1
    if lower + upper + num + others < 3:
        return 'NG'

    # 不能有长度大于2的包含公共元素的子串重复
    for i in range(len(s) - 3):
        if len(s.split(s[i:i + 3])) >= 3:
            return 'NG'
    return 'OK'


while True:
    try:
        s = input()
        print(func(s))
    except:
        break
