def decorator_func(original):
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
@counter
def original_func():
    print('original')


original_func()
original_func()