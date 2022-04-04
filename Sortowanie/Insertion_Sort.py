
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionsort1(arr):

    for i in range(1, len(arr)):
        x = arr[i]
        j = i - 1
        while j >= 0 and x < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
            # print(*arr)
        arr[j + 1] = x
        # print(*arr, sep=" ")
    # Write your code here


if __name__ == '__main__':
    # n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionsort1(arr)
    print(*arr)
