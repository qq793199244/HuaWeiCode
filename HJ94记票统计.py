def func(s1, s2):
    dic = {}
    dic['Invalid'] = 0
    for i in s1:
        dic[i] = 0
    for i in s2:
        if i in s1:
            dic[i] = dic.get(i, 0) + 1
        else:
            dic['Invalid'] += 1
    return dic


while 1:
    try:
        n1 = int(input())
        s1 = list(map(str, input().split()))[:n1]
        n2 = int(input())
        s2 = list(map(str, input().split()))[:n2]
        dic = func(s1, s2)
        for c in s1:
            print("{} : {}".format(c, dic[c]))
        print('Invalid : {}'.format(dic['Invalid']))
    except:
        break

# if __name__ == '__main__':
#     s1 = ['A', 'B', 'C', 'D']
#     s2 = ['A', 'D', 'E', 'CF', 'A', 'GG', 'A', 'B']
#     dic = func(s1, s2)
#     print(dic)  # {'Invalid': 3, 'A': 3, 'B': 1, 'C': 0, 'D': 1}
