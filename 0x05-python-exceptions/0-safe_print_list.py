#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num_printed = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            num_printed += 1
    except Exception as e:
        print("An error occurred:", str(e))        
    finally:
        print("\n")
        return num_printed
