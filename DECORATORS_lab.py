# DECORATORS


## Create a decorator that decorates a function with one argument 
# , This decorator should check that the argument is of type str and the length of the str is more than 5 ,
#  else raise an exception of type ValueError telling the user 
# the argument should be str and it should have more than 5 characters .



def decorator_function(func):
    def wrapper(*args):
        if type(*args)==str and len(*args)>5:
            return func(*args)
        else:
            raise ValueError ("argument should be str and it should have more than 5 characters")
    return wrapper

@decorator_function
def cheak_string(name):
    try:
        print("hello"+name)
    except ValueError as ve:
        print(ve)
cheak_string(input("plase enter you name:"))
