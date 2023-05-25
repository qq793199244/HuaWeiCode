def func(s):
    a, b = 0, 0
    nums = s.split(';')
    for w in nums:
        if not 2 <= len(w) <= 3:
            continue
        try:
            direction = w[0]
            step = int(w[1:])
            if direction in ['A', 'S', 'D', 'W']:
                if 0 <= step <= 99:
                    if direction == 'A':
                        a -= step
                    elif direction == 'D':
                        a += step
                    elif direction == 'S':
                        b -= step
                    elif direction == 'W':
                        b += step
        except:
            continue
    return a, b

while True:
    try:
        s = input()
        location = func(s)
        print(str(location[0]) + ',' + str(location[1]))
    except:
        break