#!/usr/bin/python3
def remove_char_at(str, n):
        tempstr = ""
        for i in range(len(str)):
                if i == n:
                        i += 1
                        continue
                tempstr += str[i]
        return tempstr
