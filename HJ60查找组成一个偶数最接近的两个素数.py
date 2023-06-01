def isPrimes(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


while True:
    try:
        num = int(input())
        half_num = num // 2
        for i in range(half_num, 1, -1):
            if isPrimes(i) and isPrimes(num - i):
                print(i)
                print(num - i)
                break
    except:
        break
