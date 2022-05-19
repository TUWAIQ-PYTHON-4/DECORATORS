
'''from msilib import type_string

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

decorator_function('hehe')'''


def str_check(fun):
    def wrapper(*args,**kwargs):
        for element in args:
            if not isinstance(element,str) or not len(element)<=5:
               raise ValueError("The parameter should be of type string and more than 5 ")
        return fun(*args,**kwargs)
    return wrapper

def add_comment(comment:str):
    print("Add your comment")

def register_user(user_name,password):
    print("Checking")
comment_input=input("Enter your comment")  
try:
    add_comment(comment=comment_input)
except Exception as e:
    print(e)

