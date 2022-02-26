def func(num):
    s = str(num)
    return s[::-1]


while 1:
    try:
        num = int(input())
        print(func(num))
    except:
        break
