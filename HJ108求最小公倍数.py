def func(A, B):
    if A < B:
        A, B = B, A
    for i in range(A, A * B + 1, A):
        if i % B == 0:
            return i


while 1:
    try:
        A, B = map(int, input().split())
        print(func(A, B))
    except:
        break
