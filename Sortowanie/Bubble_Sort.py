
def countswaps(a):
    # num = 0
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                x = a[j]
                a[j] = a[j + 1]
                a[j + 1] = x


if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    countswaps(a)
    print(a)
