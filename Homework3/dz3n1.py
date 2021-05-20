import string


def solution1(arg):
    return [i*4 for i in arg]


def solution2(arg):
    return [arg[i]*(i+1) for i in range(len(arg))]


def solution3(arg):
    return [i for i in arg if ((i % 3 == 0) or (i % 5 == 0))]


def solution4(arg):
    return [i for j in arg for i in j]


def solution5(arg):
    return [(k, i, j) for j in range(arg+1) for i in range(j) for k in range(i) if (-j**2 + i**2 + k**2) == 0]


def solution6(arg):
    return [[arg[1][j] + arg[0][i] for j in range(len(arg[1]))] for i in range(len(arg[0]))]


def solution7(arg):
    return [[arg[i][j] for i in range(len(arg))] for j in range(len(arg[0]))]


def solution8(arg):
    return [list(map(int, i.split())) for i in arg]


def solution9(arg):
    return {chr(ord('a') + v): v**2 for v in arg}


def solution10(arg):
    return {chr(ord(a[0]) + ord('A')-ord('a'))+a[1:] for a in set([b.lower() for b in arg if len(b) >= 4])}


solutions = {
    'solution1': solution1,
    'solution2': solution2,
    'solution3': solution3,
    'solution4': solution4,
    'solution5': solution5,
    'solution6': solution6,
    'solution7': solution7,
    'solution8': solution8,
    'solution9': solution9,
    'solution10': solution10,
}
# print(solution5(30))
