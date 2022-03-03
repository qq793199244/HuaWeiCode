def func(s):
    return s[::-1]


while 1:
    try:
        s = str(input())
        print(func(s))
    except:
        break
