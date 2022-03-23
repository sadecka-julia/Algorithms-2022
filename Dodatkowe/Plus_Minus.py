
def plusMinus(arr):
    p = 0
    m = 0
    z = 0
    for i in range(n):
        if arr[i] > 0:
            p += 1
        elif arr[i] < 0:
            m += 1
        else:
            z += 1
    print(round(p/n, 6))
    print(round(m/n, 6))
    print(round(z/n, 6))

    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
