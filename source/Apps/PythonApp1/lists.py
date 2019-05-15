
word = 'hello'



def func1(x):
    if x % 2 == 0:
        return x * 2
    else:
        return x * 3

list = [x**2 for x in range(1,10)]
list = [x**2 for x in range(1,10) if x % 2 == 0]
list = [func1(x) for x in range(1,10)]

def kgTOg(kg):
    return kg * 1000

kilograms = [3, 4.4, 5]
grams = [kgTOg(x) for x in kilograms]

a = [2,4,6]
b = [100, 200, 300]
c = [x*y for x in a for y in b]
print(c)