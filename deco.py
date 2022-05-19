

import errno
from logging import exception
from msilib import type_string


def word_string (func):
    def weapper(*args ,**kwargs):
        
        for element in args:
            if isinstance(element,str) or len(element):
                raise ValueError("erroe")
        
        return 
    return weapper

@word_string
def str_func(element:str):
    print("add your comment succussfuly")
    
comment =input("add your comment:")

try :
     str_func(comment)

except (exception) as o:
    print(o)
  


w_str("ahmedddd")

