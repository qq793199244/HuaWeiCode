while True:
    try:
        inputs = input().split()
        words = inputs[1:-2]
        key_word = inputs[-2]
        key_word_sort = sorted(key_word)
        res_index = int(inputs[-1])
        res = []
        for i in words:
            if i == key_word:
                continue
            if sorted(i) == key_word_sort:
                res.append(i)
        res.sort()

        print(len(res))
        if 0 <= res_index - 1 < len(res):
            print(res[res_index - 1])
    except:
        break