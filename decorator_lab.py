'''

Create a decorator that decorates a function with one argument , 
This decorator should check that the argument is of type str
and the length of the str is more than 5 ,
else raise an exception of type ValueError telling the user 
the argument should be str and it should have more than 5 characters .
'''

def check_type(func):
    def wrapper(*args,**kwargs):
        for item in args:
            if not isinstance(item, str) or len(item) <=5:
                raise ValueError("The argument should be str and it should have more than 5 characters.")
        return func(*args, **kwargs)
    return wrapper

@check_type
def add_comment(comment: str):
    
    print("add ur comment: ")

comment = input("add ur comment: ")
# calling decorator function
add_comment(comment)




    
