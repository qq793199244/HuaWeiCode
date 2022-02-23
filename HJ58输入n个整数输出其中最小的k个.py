def func(nums, k):
    nums.sort()
    return ' '.join(map(str,nums[:k]))

while 1:
    try:
        n, k = map(int, input().split())
        nums = list(map(int, input().split()))[:n]
        print(func(nums, k))
    except:
        break