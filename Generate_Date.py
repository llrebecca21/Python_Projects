'''
CIS 122 Winter 2020 Assignment 5
Author: Rebecca Lee
Credit:
Description: Create a program such that given a number between 1 and 365 or 366 inclusive and a year, it will give what date it is
'''

'''
Program Path
1. Call start()
    2. Call input_year()
    3. Call input_day_of_year()
    4. Call get_days_of_month()
        5. Call is_leap_year()
    6. Call get_date_string()
        7. Call get days_in_month()
        8. Call valid_day()



'''


def is_leap_year(year):
    """
    Check if a year provided is a leap year

    Input:
        integer value of a year

    Returns:
        True if year is a leap year or
         False if year is not a leap year
    """
    valid = False
    if year % 4 == 0 :
        if year % 100 == 0:
            if year % 400 == 0:
                valid == True
            else:
                valid == False
        else:
            valid == False
    else:
        valid == False
    return valid

def valid_year(year):
    """
    replaces year with validity checks,
    printing out any error, returning True if year is valid,
    printing False if year is invalid
    
    Must test for True or False
    """
    if year >= 0:
        return True
    else:
        print("error: year not valid")
        return False

def valid_day_of_year(day_of_year):
    """
    Replaces day validity checks, printing out any error,
    returning True if day of year is valid,
    or False if the day of year is invalid
    """
    if 0 < day_of_year <= 365:
        return True
    else:
        print("Error: day not valid")
        return False

def input_year():
    """
    Encapsulates the prompting for the year

    Args:
        None
        
    Returns:
        either 0 if the year is invalid,
        or the year as an integer.
    """
    year = input("Enter year: ")
        #if year == False:
            #return 0
            #if year == True:
    return int(year)

def input_day_of_year(year):
    """
    Encapsulates the prompting for the day of the year, and returns either 0 if the year is invalid,
    or the year as an integer.
    Must test for 0 (invalid year)
    """
    day = input("Enter day of year: ")
    # call valid_year() to check
    if valid_year(year) == True:
        return int(day)
    if valid_year(year) == False:
        return int(day)

def get_days_in_year(year):
    """
    Returns a 0 for an invalid year,
    Or the number of days in a year as an integer
    """
    valid = is_leap_year(year)
    if valid == False:
        return 0
    elif valid == True:
        if is_leap_year(year) == True:
            return 366
        else:
            return 365

def valid_month(month):
    """
    Returns True if a month is valid (0<month<=12)
    or False for an invalid month,
    with error output of "Month must be > 0"
    and "Month must be <= 12"
    """
    if 0 < month <= 12:
        return True
    else:
        print("Month must be > 0 and Month must be <= 12")
        return False

def get_full_month(month):
    if(month == 1):
        return "January"
    if(month == 2):
        return "February"
    if(month == 3):
        return "March"
    if(month == 4):
        return "April"
    if(month == 5):
        return "May"
    if(month == 6):
        return "June"
    if(month == 7):
        return "July"
    if(month == 8):
        return "August"
    if(month == 9):
        return "September"
    if(month == 10):
        return "October"
    if(month == 11):
        return "November"
    if(month == 12):
        return "Decmeber"
    else: 
        print("Must be an integer between 1 and 12", "("+str(month),"is invalid)")
        return ""

def translate_month(month):
    """
    Returns an empty string for an invalid month
    (call valid_month())
    or the month as a full month string ((e.g. January, December))
    """
    if valid_month(month) == True:
        return get_full_month(month)
    else:
        return ""

def get_days_in_month(year,month):
    """
    Returns the number of days in a month as an integer,
    accounting for leap year, or returns 0 if the year or month is invalid
    """
    if is_leap_year(year) == True:
        #print(is_leap_year(year))
        if month in [1,3,5,7,8,10,12]:
            return 31
        elif month == 2:
            return 29
        elif month in [4,6,9,11]:
            return 30
    elif is_leap_year(year) == False:
        #print(is_leap_year(year))
        if month in [1,3,5,7,8,10,12]:
            return 31
        elif month == 2:
            return 28
        elif month in [4,6,9,11]:
            return 30
    else:
        if year or month == False:
            return 0

def valid_day(year,month,day):
    """
    Returns False if the year, month or day are invalid
    or True if the arguments are valid
    """
    if valid_year(year) and valid_month(month) and valid_day_of_year(day) == True:
        return True
    elif valid_year(year) and valid_month(month) and valid_day_of_year(day) != True:
        print("Error: Either year, month or day is invalid")
        return False

def get_date_string(year,month,day):
    """
    Return:
        an empty string if the year, month, or day are invalid;
        If both are valid a string formatted as Month Day, Year (December 1, 2018)
    """
    if valid_day(year, month, day) == True:
        print("All are valid")
        return (month, str(day) + ",", year)
    else:
        if valid_day(year, month, day) == False:
            return "Error: year, month or day are invalid"

def start():
    """
    Encapsulates all of the code

    """
    # Call input_year function to set the year
    year = input_year()
    if year > 0:
        # Call input_day_of _year to supply the day
        day_of_year = input_day_of_year(year)
    # Check that both year and day_of_year are valid entries
        if year > 0 and day_of_year > 0:
            # Initialize variables
            total_days = 0
            month = 0
            day = 0
            search = True
            for i in range(12):
                if search == True:
                    # Call get_days_in_month: pass in provided year and cycle through the months
                    # get days_in_month returns: an integer value of how many days are in a given month
                    # Error in get_days_in_month
                    days_in_month = get_days_in_month(year = year, month = i + 1)
                    
                    # Based on the day entered calculate total days in the month (including month the day_of_year is in)
                    total_days += days_in_month
                    # Check if day_of_year is less than or equal to total days
                    # Otherwise keep looping
                    #print(day_of_year)
                    if (day_of_year <= total_days):
                        # Take the month value it stopped at and add one to it (fix indexing)
                        month = i + 1
                        # Calculate day of the year
                        day = days_in_month - (total_days - day_of_year)
                        # Call off Search
                        search = False  
        if month > 0 and month <= 12:
            # This is where the bug is
            print("month: ", month)
            print("year: ", year)
            print("day: ", day)
            print(get_date_string(year,month,day))

start()