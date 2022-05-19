def document_it(func):
    def wrapper(*args):
        if type(args) != str or len(args) < 5 :
            try:
                func(*args)
            except:
                print('The argument should be str and it should have more than 5 characters')
        else:
            return func(*args)
            
    return wrapper