import math

def func(num):
    dotnum = num - int(num)
    if dotnum < 0.5:
        return int(num)
    else:
        return math.ceil(num)

while 1:
    try:
        num = float(input())
        print(func(num))
    except:
        break
