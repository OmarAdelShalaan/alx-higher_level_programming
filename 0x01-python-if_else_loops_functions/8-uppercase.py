#!/usr/bin/python3
def uppercase(str):
        for i in (str):
                if i >= 'a' and i <= 'z':
                        print("{0}".format(chr(ord(i) - 32)), end = '')
                elif i >= 'A' and i <= 'Z':
                        print("{0}".format(i), end = '')

