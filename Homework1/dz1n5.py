import math
import sys


def safe_input():
    try:
        return input()
    except EOFError:
        sys.exit(0)


n = 1
s = 10000
for i in range(1, 6):
    for j in range(1, 10):
        t = n + s * j
        print('?', t, flush="True")
    print('+')
    a = n
    for j in range(1, 10):
        t = n + s * j
        if safe_input().split()[0] == "0":
            a = t
    n = a
    s = s // 10
print('!', a, flush="True")
