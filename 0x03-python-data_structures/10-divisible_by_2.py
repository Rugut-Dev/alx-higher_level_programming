#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_list = my_list.copy()
    bool_val = True

    for i in new_list:
        if i % 2 != 0:
            bool_val = False
#    print("{} {}".format(new_list, bool_val))
    return new_list, bool_val

# if __name__ == "__main__":
 #   divisible_by_2([0, 1, 2, 3, 4, 5, 6])
