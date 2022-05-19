'''
## Create a decorator that decorates a function with one argument , 
# This decorator should check that the argument is of type str and the length of the str is more than 5 ,
#  else raise an exception of type ValueError telling the user the argument should be str and it should have more than 5 characters .


'''

from unittest import result


def string_decorator(func):
    def wrapper(*args,**kwargs):
        for element in args:
            if not isinstance(element, str) and not len(element)<=5:
                raise ValueError("the parameter should be a string and 5 characters")
        return func(*args,**kwargs)
    return wrapper
    
        




def string_1(commint:str):
    print("coment added successfully")


comment=input(("add ur comment:"))
try:
    string_1(comment)
except Exception as e:
    print(e)

      
