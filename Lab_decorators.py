# DECORATORS


## Create a decorator that decorates a function with one argument , 
# This decorator should check that the argument is of type str and the length of the str is more than 5 , 
# else raise an exception of type ValueError telling the user the argument should be str and it should have more than 5 characters .

# decorator 
def check_str(func):
    # wrapper
    def inner(*args):
        print('inside wrapper before excuting')
        func(*args)
        print(args)
        print(len(args))
        if isinstance(args, str) and len(args) > 5:
            print('String with more than 5 chars')
        else:
            raise ValueError("You should enter string more than 5 chars")
        print('inside wrapper after excuting')
    return inner

# The Actual function
def my_func(txt):
    print(len(txt))
    print('inside actual function')
    
    
# passing 'my_func' inside the
# decorator to control its behaviour
my_func = check_str(my_func)
 
 
# calling the function
my_func('Hello World')


### didn't work exactly
## in the wrapper (inner) - the arge len = 1 ! couldn't fix it !
