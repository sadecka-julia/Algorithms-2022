import math
import os
import random
import re
import sys


def countswaps(a):
    num = 0
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                num = num + 1
                x = a[j]
                a[j] = a[j + 1]
                a[j + 1] = x

        print('Pierwszy:', a[0])
        print('Ostatni', a[-1])
        print('Ciąg', a)
        print('Liczba:', num)


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))
    print(n, 'Lista', a)

    countswaps(a)
    print()
