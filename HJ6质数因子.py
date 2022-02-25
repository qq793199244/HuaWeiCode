def func(num):
    res = []
    if num <= 1:
        return
    for i in range(2, int(num ** 0.5) + 1):
        while num % i == 0:
            res.append(i)
            num //= i
    if num > 1:
        res.append(num)
    return ' '.join(map(str, res))


while 1:
    try:
        num = int(input())
        print(func(num))
    except:
        break

# if __name__ == '__main__':
#     print(func(64577))
#     print(func(93938))
#     print(func(180))
#     print(func(2000000014))
