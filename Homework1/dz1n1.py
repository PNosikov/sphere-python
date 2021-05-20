n = int(input())
a = input().split()
ind = [0] * 100000
count = 0
for i in a:
    if not ind[int(i)]:
        print(i, end=' ')
        count += 1
    ind[int(i)] = 1

print('\n', len(a)-count, sep='')
