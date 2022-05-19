class ValueError(Exception):
    pass

def check_decorator(func):
    def wraper(args: str):
        if type(args) != str or len(args) < 5:
             raise ValueError('only enter string with more than 4 char')
        else:
            func(args)

    return wraper


# adding decorator to the function
@check_decorator
def print_if_str(string: str):
    print(string)


print_if_str('hello')
    
