#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    n = len(args)
    if n == 0:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(n, '' if n == 1 else 's'))
        for i, arg in enumerate(args, 1):
            print("{}: {}".format(i, arg))
