def func(s):
    return len(s.split()[-1])


while 1:
    try:
        s = input()
        print(func(s))
    except:
        break
