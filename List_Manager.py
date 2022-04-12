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
def cmd_add(t):
    """
    Summary: After add is typed as the command, the input is added to the list
    Input: list
    Output: none
    Return: return the length of the new appended list
    """
    new_t = t.append(y)
    return len(t)

# Create a cmd_delete function
def cmd_delete(t):
    """
    Summary: prints list of t at each point in del command
    Input: t
    Output: prints current t list and index
    Return: empty
    """
    label_spacing = 5
    num_spacing = 5
    for index in range(len(t)):
        index_2 = index
        print(pad_right(index, label_spacing), pad_left(t[index_2], num_spacing))
    return ""

# Create a cmd_list function
def cmd_list(t):
    """
    Summary: prints the number of items in the list t and prints which elements are included in the list
    Input: list t
    Output: prints len(t) and items in t
    Return: empty
    """
    print("List contains", len(t), "item(s)")
    for item in t:
        print(item)
    return ""



# Create a cmd_clear function
def cmd_clear(t):
    """
    Summary: clears the current list t
    Input: list t
    Output: prints how many items are deleted
    Return: empty
    """
    h = len(t)
    delete_t = t.clear()
    print(h, "item(s) removed, list empty")
    return ""

# Create a get_max_list_item_size function
def get_max_list_item_size(t):
    """
    Summary: Checks which item in command list is longest
    Input: list t
    Output: empty
    Return: length of the longest item in the list plus 5
    """
    command_short = ["Add", "Delete", "List", "Clear"]
    t = command_short
    length = 0
    for item_list in command_short:
        if len(item_list) == 0:
            return ""
        if len(item_list) > -1 and (len(item_list) > length):
            long_length = item_list
            length = len(long_length)
    return length + 5


# Create a program that will iterate through the program











