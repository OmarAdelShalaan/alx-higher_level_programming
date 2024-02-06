#!/usr/bin/python3
if __name__  == "__main__":
        from calculator_1 import add, mul, sub, div 
        import sys
        count = len(sys.argv)
        if count != 4:
                print("Usage: ./100-my_calculator.py <a> <operator> <b>")
                exit("1")
        else:
                if sys.argv[2] == "+":
                        print("{} + {} = {}".format(int(sys.argv[1]), int(sys.argv[3]), add(int(sys.argv[1]), int(sys.argv[3]))))
                elif sys.argv[2] == '-':
                        print("{} - {} = {}".format(int(sys.argv[1]), int(sys.argv[3]), sub(int(sys.argv[1]), int(sys.argv[3]))))
                elif sys.argv[2] == '*':
                        print("{} * {} = {}".format(int(sys.argv[1]), int(sys.argv[3]), mul(int(sys.argv[1]), int(sys.argv[3]))))
                elif sys.argv[2] == '/':
                        print("{} / {} = {}".format(int(sys.argv[1]), int(sys.argv[3]), div(int(sys.argv[1]), int(sys.argv[3]))))
