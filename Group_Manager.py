"""
CIS 122 Winter 2020 Assignment 8
Author: Rebecca Lee
Credit: Greyson
References:https://stackoverflow.com/questions/30362391/how-do-you-find-the-first-key-in-a-dictionary
Description: Create a group manager
"""

#Group manager will do the following:
    #Create a new group by group name and defining properties
    #Add data to a group
    #List groups
    #List data for a group
    #Display help screen with commands

#Use lists and dictionaries to store group info

#Use a list when you want to just store data
#Use a dictionary when you want to store data by a name
"""
{
    'group_name':{
        '_keys_': [],
        '_data_': [ { }, { } ...],
    },
    ...
}
"""

#Declare group variable:
d = {}

def get_help():
    """
    Summary: lists what commands are allowed
    Input: none
    Output: list of commands
    Return: empty
    """
    print("***Available Commands***")



    print("?:", "list commands")
    print("C:", "Create a new group")
    print("A:", "Add data to a group")
    print("G:", "List groups")
    print("L:", "List data for a group")
    print("X:", "Exit")
    return ""







#command == c function from TA
#This function works properly
def create_group(d):
    """
    Summary: Creates a group
    Input: d
    Output: updated group d
    Returns: none
    """
    print("** Create New Group **\n")
    while True:
        name = input ("Enter group name (empty to cancel):")
        if name in d:
            print("name already exist")
        elif len(name.strip())== 0:
            break
        else:
            # d[name]['_keys_']=[] and replace all temp_keys with this.
            temp_key = []
            temp_dict = {}
            while True:
                key = input("Enter field name (empty to stop):")
                if len(key.strip()) == 0:
                    break
                temp_key.append(key)
            '''
            d[name]['_keys_'] = temp_key
            d[name]
            '''
            temp_dict['_keys_'] = temp_key
            temp_dict['_data_'] = []
            d[name] = temp_dict
    print(d)
    return ""



def list_groups(d):
    """
    Summary: List group names and number of properties
    Input: d
    Output: list of groups
    Returns: empty
    """
    print("**List of Groups**")
    
    print(next(iter(d)), ":", len(d.values()),"properties" ) #TODO list the properties of the group
    return ""

#A  
def add_group_data(d):
    """
    Summary: Adds data to a group for each group property
    Input: d
    Output: none
    Returns: d
    """
    print("** Add group data **")
    #Adds data to a group for each group property
    print(list_groups(d))
    while True:
        y = input("Enter group (empty to cancel):")
        if len(y.strip()) == 0:
            break
        elif y.strip() not in d:
            print("Group does not exist, enter group that already exists")
        elif y.strip() in d:
            i = range(0,10)
            for i in d[y]['_keys_']: #Not sure at this point
                keys = d[y]['_keys_'][0]
                new_key = input("Enter " + str(keys)+ ":")
                d = d[new_key]
                return d
                #return(d[new_key])
                
            
            
            '''
            #for index, element in enumerate('abc')
                print(index, element)
            '''   
                
            
    
#Fix the print statement    

def list_group_data(d):
    """
    Summary: List all data for a group
    Input: d
    Output: data in dictionary
    Returns: none
    """
    #List all data for a group
    print(list_groups(d))
    group_name = input("Enter group name (empty to cancel):")
    if group_name == "":
        return ""
    else:
        if group_name not in d:
            print("Error group name not in group")
        else:
            if group_name in d:
                i = range(1,10)
                for i in d[group_name]:
                    print(enumerate, d[group_name][i])             
    
 
    
            
'''
group = {}
#create_group(group)
print(group)
'''
    
    



    
print(">> Welcome to Group Manager <<\n This program creates groups with dynamic properties \n")

while True:
    y = input("Command (empty or X to quit, ? for help):")
    z = y.strip()
    command = z.upper()
    if command =="" or (command == "X"):
        print("Goodbye")
        break

    elif command == "?":
        print(get_help())

    elif command == "C":
        print(create_group(d))

    elif command == "G":
        print(list_groups(d))

    
    elif command == "A":
        print(add_group_data(d))

    elif command == "L":
        print(list_group_data(d))
        
            
        

"""
Week 10 lab notes
"""

'''
How to locate certain parts in the example at beginning of assignment
G[S]['_keys_'][0] -> Loc_T

G[S]['_data_'][0][Lock_T] -> Song
    ....        [Lock_A] -> name
'''
