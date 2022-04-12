'''
CIS 122 Winter 2020 Lab 08
Author: Rebecca Lee
Credit:
Description: Create a random number generator
"Work in Progress"
'''

# Import random
import random

# Create gen_random_integer_list or (gril for short) function
def gril(num,start_range = 1, end_range = 100, sort_list = 'N'):
    """
    Summary: When definition is called it will create a random integer list

    param num: number of integers in the list
    param start_range: min value in the list
    param end_range: max_value in the list
    param sort_list: If Y then sort list, if N do not sort
    """
    #Return variable
    t = []

    # parameter check
    if num <= 0:
        print("num must be > 0")
    elif not isinstance(num,int):
        print('num must be an integer')
    elif not isinstance(start_range, int) or not isinstance(end_range, int):
        print('start_range and end_range must be integers')
    else:
        for i in range(num):
            r = random.randint(start_range,end_range)
            t.append(r)
        if sort.list.upper == 'Y':
            t.sort()
    return t
