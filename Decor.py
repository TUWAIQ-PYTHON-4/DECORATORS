

def checkS(func):
    def wrapper(*args):
        for i in args:
            if not isinstance(i,str)or len(i)<=5:
                raise ValueError("The parameter should be of type str")
            return func(*args)
        return wrapper

@checkS
def add_comment(comment:str):
    print("add your comment succussfully")

comment_input=input("add your comment:")
try :
     add_comment(comment_input)

except Exception as e:
    print(e)



