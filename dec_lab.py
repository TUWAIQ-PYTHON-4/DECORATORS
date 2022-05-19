from msilib import type_string


def decorator_function(func):
    def wrapper(*args, **kwargs):
        try : 
          func(*args, **kwargs)
          if type_string() != decorator_function & len(decorator_function) <= 5:
           print("")
        except (ValueError,TypeError):
          print("invalid or your string is less than 5")    
    return wrapper

def str_func(element:str):
    print(element)
    raise ValueError("Error")

decorator_function('hehe')