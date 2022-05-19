# DECORATORS


## Create a decorator that decorates a function with one argument , 
# This decorator should check that the argument is of type str and the length of the str is more than 5 , 
# else raise an exception of type ValueError telling the user the argument should be str and it should have more than 5 characters .

def check_argue_decorator(func):
    def wrapper(*args):
        if args is str and len(args) > 5:
            print('Its a string with more than 5 chars')
        else:
            raise Exception("You should enter string more than 5 chars")
        return func(*args)
    return wrapper

@check_argue_decorator
def func(*text):
    a = text
    return a

user_input = input('Enter a string with more than 5 chars ...')

func(user_input)

