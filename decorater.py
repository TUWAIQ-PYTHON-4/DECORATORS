
def new_decorater(func):
    def wrpper (*args , **kwargs):
        for elemnt in args :
            if type(elemnt) != str or len(elemnt) <= 5:
                raise ValueError("The argument should be str and it should have more than 5 characters .")
        
        result = func (*args,**kwargs)
        return result
    return wrpper  

@new_decorater
def ckeck_str (coment:str ):
    print(" the commnt is seccessfuly") 
     
coment_user = input(" Enter your coment : ")

try :
    ckeck_str(coment_user)
except ValueError as v: 
    print(v)