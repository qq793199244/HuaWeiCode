def func(s):
    res = s.split()
    return ' '.join(res[::-1])


while 1:
    try:
        s = str(input())
        print(func(s))
    except:
        break
