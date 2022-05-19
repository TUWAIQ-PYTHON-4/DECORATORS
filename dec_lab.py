

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

