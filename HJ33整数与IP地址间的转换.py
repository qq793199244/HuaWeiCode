while True:
    try:
        ip = input().split('.')
        # 十进制转32位二进制
        ip_10 = bin(int(input()))[2:].zfill(32)
        # 处理二进制IP
        res_2 = []
        for i in ip:
            res_2.append(bin(int(i))[2:].zfill(8))
        print(int("0b" + "".join(res_2), 2))

        # 处理十进制IP
        res_10 = []
        for i in range(0, len(ip_10), 8):
            res_10.append(str(int("0b" + ip_10[i : i + 8], 2)))
        print(".".join(res_10))
    except:
        break