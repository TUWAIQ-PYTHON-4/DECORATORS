
def check(func):
    def wrapper(*args):
    
        if type(*args) !=  str and len(*args) <5:
            return func(*args)
        else:   
            raise ValueError("the argument should be str and it should have more than 5 characters ")
            
    return wrapper




@check
def user_input(str_user:str):
    print(" your string :" , str_user)
try:
    user_input("hi i am ruba")
except Exception as e :
    print(e)