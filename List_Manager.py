'''
CIS 122 Winter 2020 Assignment 5
Author: Rebecca Lee
Credit:
Description: Create a basic list manager program
'''

# Create a list variable

t = []

# All the functions that are called
# Create pad_string function
def pad_string(data, size, dir = 'L', chr = ' '):
    data = str(data)
    if len(data) > size:
        return data
    elif dir.upper() == 'L':
        return chr * (size - len(data)) + data
    else:
        return data + chr * (size - len(data))

# Create pad_left function
def pad_left(data,size,chr = ' '):
    return pad_string(data, size, 'L', chr)

# Create pad_right function
def pad_right(data, size, chr = ' '):
    return pad_string(data, size, 'R', chr)

# Create a command list

# Create cmd_help function

# Create a cmd_add function

# Create a cmd_delete function

# Create a cmd_list function

# Create a cmd_clear function

# Create a get_max_list_item_size function

# Create a program that will iterate through the program











