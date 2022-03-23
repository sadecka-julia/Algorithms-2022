

def mergeSort(arr, l, p):
    if l >= p:
        return
    m = (l+p)//2
    mergeSort(arr, l, m)
    mergeSort(arr, m+1, p)
    merge(arr, l, p, m)


def merge(arr, l, p, m):

    i = j = 0
    k = l
    lewy_arr = arr[l:m+1]
    prawy_arr = arr[m+1:p+1]
    while i < len(lewy_arr) and j < len(prawy_arr):
        if lewy_arr[i] >= prawy_arr[j]:
            arr[k] = prawy_arr[j]
            j += 1
        else:
            arr[k] = lewy_arr[i]
            i += 1
        k += 1
    while i < len(lewy_arr):
        arr[k] = lewy_arr[i]
        i += 1
        k += 1
    while j < len(prawy_arr):
        arr[k] = prawy_arr[j]
        j += 1
        k += 1

if __name__ == '__main__':
    arr = [9, 8, 7, 6, 5, 4, 3, 2, 11, 0, 4, 3, 9, 91, 102, 4]
    print('Ciąg na początku: \n', arr)
    mergeSort(arr, 0, len(arr)-1)
    print('Ciąg na końcu: \n', arr)
