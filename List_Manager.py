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
command_list = ["Add", "Delete", "List", "Clear", "Empty to exit"]

# Create cmd_help function
def cmd_help():
    """
    Summary: gives the available list of commands accepted
    Input: empty
    Output: avaliable list of commands and what they do
    Return: empty
    """
    print("***Available Commands***")

    label_spacing = 10
    num_spacing = 10

    print(pad_right(command_list[0], label_spacing), pad_left("Add to list", num_spacing))
    print(pad_right(command_list[1], label_spacing), pad_left("Delete information", num_spacing))
    print(pad_right(command_list[2], label_spacing), pad_left("List information", num_spacing))
    print(pad_right(command_list[3], label_spacing), pad_left("Clear list", num_spacing))
    print(pad_right(command_list[4], label_spacing))
    return ""
    
# Create a cmd_add function

# Create a cmd_delete function

# Create a cmd_list function

# Create a cmd_clear function

# Create a get_max_list_item_size function

# Create a program that will iterate through the program











