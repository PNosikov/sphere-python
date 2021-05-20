def chain_loop(args):
    check = {}
    list1 = args
    list1 = list(filter(lambda x: bool(x), args))
    list1 = list(map(iter, list1))
    for i in range(len(list1)):
        check[i] = 0
    j = 0
    k = 0
    while (j >= 0):
        try:
            for i in range(k, len(list1)):
                if check[i] == 0:
                    yield next(list1[i])
            k = 0
        except (StopIteration):
            k = i + 1
            check[i] = 1
            continue
        flag = 1
        for i in range(len(list1)):
            if (check[i] == 0):
                flag = 0
        if (flag == 1):
            j = -1


# from itertools import tee
# a = (i for i in range(3))
# print(list(chain_loop(tee(a, 5))))
