def func(nums, rule):
    if rule == 0:
        return ' '.join(map(str, sorted(nums)))
    if rule == 1:
        return ' '.join(map(str, sorted(nums)[::-1]))


while 1:
    try:
        n = int(input())
        nums = list(map(int, input().split()))[:n]
        rule = int(input())
        print(func(nums, rule))
    except:
        break
