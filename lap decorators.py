def document_it(func):
    def wrapper(*args):
        if type(*args) == str and len(*args) > 5:
            return func(*args)
        else:
            raise ValueError('The argument should be str and it should have more than 5 characters')

    return wrapper


@document_it
def unser_input(user_var: str):
    print(user_var)


unser_input("hi there")
