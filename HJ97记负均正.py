def func(nums):
    neg_count = 0
    pos_count = 0
    pos_sum = 0
    for num in nums:
        if num < 0:
            neg_count += 1
        if num > 0:
            pos_sum += num
            pos_count += 1
    return '{} {:.1f}'.format(neg_count, pos_sum / pos_count)


while 1:
    try:
        n = int(input())
        nums = list(map(int, input().split()))[:n]
        print(func(nums))
    except:
        break
