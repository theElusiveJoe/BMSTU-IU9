#!/bin/python3

import sys
import random


def print_strings(num, length):
    symbols = "\"qwertyuiop[]asdfghjkl;'zxcvbnm," \
              "./1234567890-=!@#$%^&*()_+QWERTYUIOP" \
              "{}ASDFGHJKL:ZXCVBNM<>?"
    leng = len(symbols)-1
    for i in range(num):
        res = ''
        for j in range(length):
            res += symbols[random.randint(0, leng)]
        print(res)


print_strings(int(sys.argv[1]), int(sys.argv[2]))
