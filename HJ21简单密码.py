def func(s):
    res = ''
    for c in s:
        if '0' <= c <= '9':
            res += c
        elif c.isupper() and c != 'Z':
            # chr() 返回值是当前整数对应的 ASCII 字符
            # ord() 返回值是对应的十进制整数
            res += chr(ord(c.lower()) + 1)
        elif c == 'Z':
            res += 'a'
        elif c in 'abc':
            res += '2'
        elif c in 'def':
            res += '3'
        elif c in 'ghi':
            res += '4'
        elif c in 'jkl':
            res += '5'
        elif c in 'mno':
            res += '6'
        elif c in 'pqrs':
            res += '7'
        elif c in 'tuv':
            res += '8'
        elif c in 'wxyz':
            res += '9'
    return res


while 1:
    try:
        s = str(input())
        print(func(s))
    except:
        break
