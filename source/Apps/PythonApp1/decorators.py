from functools import wraps

def decorator_func(original):
    @wraps(original)
    def wrapper():
        print('wrapper')
        original()
    return wrapper

def counter(func):
    def wrapper():
        wrapper.count += 1
        func()
        print(wrapper.count)
    wrapper.count = 0
    return wrapper

@decorator_func
#@counter
def original_func():
    '''docstring1'''
    print('original')


original_func()
print(original_func.__name__)
print(original_func.__doc__)