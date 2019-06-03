def create_cubes(n):
    for x in range(n):
        yield x**3

#print(create_cubes(10))

def fib(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a+b

#g = fib(3)
#print(next(g))
#print(next(g))git 
#print(next(g))
#print(next(g))
   
def iterator():
    s_iter = iter('hello')
    print(next(s_iter))

#list() iter()

list = [1,3,5,7,9]
#l = [x**2 for x in list if x > 3] #list comprehension
g = (x**2 for x in list if x > 3) #generator comprehension
print(g)
