
from logging import exception
from operator import ge
from unittest import result
from xml.etree.ElementTree import Comment


# create decorator:
def checkString(func):
    def wrapper(*args):
        result = func (*args)
        for elemnt in args :
            if type(elemnt) != str or len(elemnt) <= 5:
                raise ValueError("The arg should be string and len at least 5 charcter")
            else:
                print("checking successful")    
            return func (*args)
    return wrapper       

@checkString
def get_name(name:str):
    pass


try:
    get_name("Abdulaziz") # if the parameter not string OR less than 5 charcter, recevice ValueError

except Exception as e:
    print(e)



