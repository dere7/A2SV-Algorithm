#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countInversions' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def _mergeSort(arr, start, end, inversions=0):
    n = end - start
    if n == 0 or n == 1:
        return 0
    # divide
    mid = n // 2
    inversions += _mergeSort(arr, start=start, end=mid)
    inversions += _mergeSort(arr, start=mid + 1, end=end)

    # conquer/merge using insertion sort
    for i in range(1, n + 1):
        for j in range(i, 0, -1):
            if arr[j - 1] > arr[j]:
                temp = arr[j - 1]
                arr[j - 1] = arr[j]
                arr[j] = temp
                inversions += 1
    return inversions

def countInversions(arr):
    return _mergeSort(arr, start=0, end=len(arr) - 1)

if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        print(str(result))

