# DECORATORS


## Create a decorator that decorates a function with one argument , 
# This decorator should check that the argument is of type str and the length of the str is more than 5 , 
# else raise an exception of type ValueError telling the user the argument should be str and it should have more than 5 characters .

# decorator 
def check_str(func):
    # wrapper
    def inner(*args,**kwargs):
        # Operations 
        func(*args,**kwargs)
        for element in args:
            if isinstance(element, str) and len(element) > 5:
                print('Work sccussfully')
            else:
                raise ValueError("You should enter string more than 5 chars")
                
                
    return inner

# The Actual function
def my_func(txt):
    pass
    
    
    
# passing 'my_func' inside the
# decorator to control its behaviour
my_func = check_str(my_func)
 
# Taking Input from the user
u_input = input('Enter a string with more than 5 chars .. ')
# calling the function
my_func(u_input)



