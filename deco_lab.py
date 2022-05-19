

def string_deco(func):
    def wrapper(*args):
        if type(*args) == str and len(*args) > 5:
            return func(*args)
        else:
           raise ValueError ('should be str and it should have more than 5 characters')     
    return wrapper


@string_deco
def print_word(word):
    print(word)

try:
    print_word('eduction')

except ValueError as v:
    print(v)