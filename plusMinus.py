#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    lenArr = len(arr)
    posCount = 0
    negCount = 0
    zeroCount = 0
    for i in range(lenArr):
        if arr[i] > 0:
            posCount += 1
        elif arr[i] < 0:
            negCount += 1
        else:
            zeroCount += 1
    posAvrg = posCount / lenArr
    negAvrg = negCount / lenArr
    zeroAvrg = zeroCount / lenArr
    print(posAvrg)
    print(negAvrg)
    print(zeroAvrg)
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
