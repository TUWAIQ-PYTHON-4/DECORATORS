from re import A


def decr(enter_phrase):
    def wrapper(*args):
        if type(*args) != str:
            raise ValueError("the argument should be str and it should have more than 5 characters")
        elif len(*args) <= 5:
            raise ValueError("the argument should be str and it should have more than 5 characters")
        else:
            print("good phrase ")
        return enter_phrase(*args)
    return wrapper

@decr
def enter(phrase):
    print(phrase)
try:
    enter(input("enter phrase: "))
except ValueError as error:
    print(error)
