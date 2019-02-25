'''
The following functions are all intended to check whether a string
contains any lowercase letters, but at least some of them are wrong.
For each function, write its docstring to describe what the function
actually does (assuming that the parameter is a string).



'''


def any_lowercase1(s):
    """This function evaluates the first character and returns True when it is lowercase and False when it is not."""
    for c in s:
        if c.islower():
            return True
        else:
            return False


def any_lowercase2(s):
    """This function always returns True, since 'c' a local string is evaluated only, and not the input.'"""
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'


def any_lowercase3(s):
    """This function returns whether the last character is lower as True, or upper as False"""
    for c in s:
        flag = c.islower()
    return flag


def any_lowercase4(s):
    """This function evaluates each character in the string (s) and returns True when one is lower. """
    flag = False
    for c in s:
        flag = flag or c.islower() #it assigns the value True when one of the variables is True.
    return flag


def any_lowercase5(s):
    """This function returns False when there is an upper charachter, When all are lower it returns True"""
    for c in s:
        if not c.islower():
            return False
    return True
