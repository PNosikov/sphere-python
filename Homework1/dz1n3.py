import math

a = float(input())
ist = a
b = a // 10.00
a = a - b * 10.00
c = a // 5.00
a = a - c * 5.00
d = a // 2.00
a = a - d * 2.00
e = a // 1.00
a = a - e * 1.00
f = a // 0.50
a = a - f * 0.50
g = a // 0.10
a = a - g * 0.10
h = a // 0.05
a = a - h * 0.05
j = a / 0.01
a = a - j * 0.01
# print(a)
if b > 0:
    print("10.00", int(b), sep='\t')
if c > 0:
    print(" 5.00", int(c), sep='\t')
if d > 0:
    print(" 2.00", int(d), sep='\t')
if e > 0:
    print(" 1.00", int(e), sep='\t')
if f > 0:
    print(" 0.50", int(f), sep='\t')
if g > 0:
    print(" 0.10", int(g), sep='\t')
if h > 0:
    print(" 0.05", int(h), sep='\t')
if j >= 0.9:
    print(" 0.01", int(j + 0.1), sep='\t')
