#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Prints x elements from list"""
    try:
        new_list = my_list[:x]
        num = 0
        for i in new_list:
            print("{}".format(i), end="")
            num += 1
    except Exception:
        print("Error Occured\n")
    finally:
        print()
        return num
