#!/bin/python

import math
import os
import random
import re
import sys



#
# Complete the 'oddNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER r
#

def oddNumbers(l, r):
    # Write your code here
    result = []
    for i in range(l,r + 1):
        if i % 2 == 1:
            result.append(i)
    return result
def main():
    print(oddNumbers(3, 5))
main()