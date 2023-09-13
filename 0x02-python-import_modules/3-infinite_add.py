#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv)
    argv_list = sys.argv
    total = 0
    if n == 1:
        print(0)
    else:
        for i in range(1, n):
            total = total + int(argv_list[i])
        print(total)
