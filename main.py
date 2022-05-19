

def check_function(func):
    def wrapper(*args, **kwargs):
     for element in args :
         if not isinstance(element, str) or len(element)<=5:
            raise ValueError("please fill in a valid phrase") 
         
   
     return func (*args, **kwargs)
    return wrapper

@check_function
def your_word(word:str):
 print("add succussfully")

word = input("Enter you word")

try:your_word(word)
except ValueError as a:
       print(a)

