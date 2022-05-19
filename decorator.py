def deco(func):
    def wrapper(*ar):
        if type(*ar) == str and len(*ar) >= 5:
            return func(*ar)
        else:
            raise ValueError("the argument should be str and it should have more than 5 characters") 
    return wrapper

@deco
def print_name(name):
    print("Hello ", name) 

try:
    print_name(77)
except ValueError as n:
    print(n)






