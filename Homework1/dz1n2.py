def summa_tsifr(k):
    s = 0
    while k:
        s += k % 10
        k = k // 10
    return s


def main():
    n = int(input())
    arr1 = [int(i) for i in input().split()]
    arr2 = [0]*n
    for i in range(n):
        arr2[i] = summa_tsifr(arr1[i])
    arr3 = sorted(arr1, key=lambda i: (summa_tsifr(i), i))
    for i in range(n):
        print(arr3[i], end=' ')


if __name__ == "__main__":
    main()
