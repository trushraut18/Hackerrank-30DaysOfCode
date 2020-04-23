#!/bin/python

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    if n==0:
        return 1
    if n>0:
        return n*factorial(n-1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
