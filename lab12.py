
def decorator_function(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

@decorator_function
def is_str():
    s=input()
    if type(s) != str or len(s)<5 :
        raise Exception("the argument should be str and it should have more than 5 characters")
    

try:
 decorated_function = decorator_function(is_str)
 decorated_function()
except Exception as ve:
    print(ve)
