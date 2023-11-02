#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv) < 2:
        sum = 0
    else:
        sum = 0
        for i in range(len(argv)):
            if i == 0:
                pass
            else:
                sum += int(argv[i])
    print("{}".format(sum))
