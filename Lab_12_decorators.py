

'''
## Create a decorator that decorates a function with one argument , 
# This decorator should check that the argument is of type str 
# and the length of the str is more than 5 ,
#  else raise an exception of type ValueError telling the user 
# the argument should be str and it should have more than 5 characters .
'''


from curses import wrapper
from unittest.loader import VALID_MODULE_NAME


def check_char(check):
    def wrapper(*args, **kwargs):
        if  type(*args, **kwargs) == str and len(*args, **kwargs) > 5:
          print("The caracter is string and more 5")
        else:
          raise ValueError('Error ValueError')
        return check
    return wrapper
    

@check_char
def characters(char):
    print(char)


try :
    characters("mohammed")
except ValueError as err:
    print(err)


