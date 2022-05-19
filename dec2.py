def check(func):
    def wrapper(*args):

        if type(*args) !=  str or len(*args) <5:
            raise ValueError("the argument should be str and it should have more than 5 characters ")


        else:   
            return func(*args)
    return wrapper


@check
def user_input(str_user:str):
    print(" your string :" , str_user)
try:
    user_input("hello")
except Exception as e :
    print(e)