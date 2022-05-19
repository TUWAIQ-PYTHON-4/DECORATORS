
def decorator_function(func):
    def check(*args, **kwargs):
        if type(*args) != str or len(*args) < 5:
            raise Exception("the argument should be str and it should have more than 5 characters")
        else:
            return func(*args)

    return check
            
@decorator_function
def is_str(s):
    print("doing operation")

try:
    s=input()
    is_str(s)
except Exception as ve:
    print(ve)
