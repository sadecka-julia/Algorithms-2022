

def partition(arr, l, p):
    pivot = arr[p]
    i = l - 1
    for j in range(l, p):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[p] = arr[p], arr[i+1]
    return i+1
def quicksort(arr, l, p):
    if l < p:
        q = partition(arr, l, p)
        print(*arr, sep=" ")
        quicksort(arr, l, q-1)
        quicksort(arr, q+1, p)


if __name__ == "__main__":
    n = input()
    tab = list(map(int, input().rstrip().split()))
    quicksort(tab, 0,  len(tab)-1)
