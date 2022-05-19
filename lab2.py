import string


def document_it(func):
    def wrapper(*args, **kwargs):
        for ele in args:
            if not isinstance(ele, str)or not len(ele)<=5:
                raise ValueError("error string")
        return func(*args, **kwargs)
    return wrapper


@document_it
def srt_func(string:str):
    print("enter your string")
    ss=input("enter string ")
    srt_func("Abdulhadi")

try:
    srt_func("Abdulhadi")
except ValueError as e:
    print("In your string error")