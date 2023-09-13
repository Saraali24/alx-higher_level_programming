#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv)
    argv_list = sys.argv
    if n == 1:
        print("0 arguments.")
    elif n == 2:
        print("1 argument:\n"+(f"1: {argv_list[1]}"))
    else:
        print(f"{n-1} arguments:")
        for i in range(1, n):
            print(f"{i}: {argv_list[i]}")
