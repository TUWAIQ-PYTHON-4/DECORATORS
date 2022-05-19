def decorator_function(func):
    def checktype(*args, **kwargs):
        for i in args:
         if type(i)!=str or len(i)<=5:
             raise ValueError("you shoud entes string and have more than 5 characters")
         return func(*args, **kwargs)
    return checktype

value=input("Enter String:")
@decorator_function
def print_value(value:str):
    print(value)

#calling decorated function
try:
    print_value(value)
except ValueError as e:
    print(e)