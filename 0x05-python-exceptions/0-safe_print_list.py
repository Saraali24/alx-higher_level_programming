#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num_printed = 0
    try:
        for i in range(x):
            print(my_list[i], end=" ")
            num_printed += 1
    except IndexError:
        print("Erorr: Index out of range!")
    finally:
        return num_printed
        print()
