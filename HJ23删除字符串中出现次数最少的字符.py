def delete_c(s):
    dic = {}
    res = ''
    for c in s:
        if c not in dic:
            dic[c] = 1
        else:
            dic[c] += 1
    min_count = min(dic.values())
    for c in s:
        if dic[c] != min_count:
            res += c
    return res

while True:
    try:
        s = input()
        print(delete_c(s))
    except:
        break