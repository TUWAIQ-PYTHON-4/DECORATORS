from msilib import type_string


def decorator_function(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper


def str_func(element:str):
    print(element)
    raise ValueError("Error")

try :
  decorator_function('heh')
  if type_string() != decorator_function & len(decorator_function) <= 5:
    print("")
except (ValueError,TypeError):
    print("invalid or your string is less than 5")


decorator_function('hehe')