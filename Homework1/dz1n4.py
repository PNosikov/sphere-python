import math

n, k = map(int, input().split())
s = 0
count = 0
m = n
if k == 0:
    print("0")
else:
    while m > 0:
        m = m // 10
        count += 1
    for i in range(k):
        s += n * (k-i) * (10 ** (count*i))
if k > 0:
    print(int(s))
