def square(x):
    return x ** 2

def isEven(x):
    return x % 2 == 0

squareL = lambda num: num ** 2

list1 = [1,2,3,4]
#squareList = map(square, list1)
#print(list(squareList))
list2 = filter(isEven, list1)

list3 = filter(lambda x: x % 2 == 1, list1)

print(list(list3))
