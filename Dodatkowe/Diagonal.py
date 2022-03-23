
import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    print(arr)
    l = 0
    p = 0
    for i in range(n):
        l += arr[i][i]
        p += arr[i][-(i+1)]
    result = abs(l-p)
    print(l, p, result)

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))


    result = diagonalDifference(arr)

