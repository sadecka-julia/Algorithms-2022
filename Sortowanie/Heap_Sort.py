
def maxHeapify(arr, i, n):
    l_dziecko = 2*i + 1
    p_dziecko = 2*i + 2
    if n >= l_dziecko and arr[i] < arr[l_dziecko]:
        largest = l_dziecko
    else:
        largest = i
    if n >= p_dziecko and arr[largest] < arr[p_dziecko]:
        largest = p_dziecko
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        maxHeapify(arr, largest, n)


def buildMaxHeap(arr, n):
    for i in range(n//2, -1, -1):
        maxHeapify(arr, i, n)


def heapSort(arr, n):
    buildMaxHeap(arr, n)
    for i in range(n, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        maxHeapify(arr, 0, i-1)


if __name__ == "__main__":
    arr = [0,12,4,2,9,0,87,122,54,1,2,11,55,99]
    n = len(arr) - 1
    heapSort(arr, n)
    print(*arr)
