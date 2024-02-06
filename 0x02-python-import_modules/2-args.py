#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len(sys.argv) - 1
    if count == 1:
        print("{:d} argument:".format(count))
    elif count == 0:
        print("{:d} arguments.".format(count))
    else:
        print("{:d} arguments:".format(count))
    for i in range(1, count + 1):
        print("{:d}: {}".format(i, sys.argv[i]))
