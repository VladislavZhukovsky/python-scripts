import math

def dataTypes():
    x = 3
    y = 3.4
    b = False
    s = 'string'

    list = [1,2,3,4]
    dict =  {1:'11', 2:'22'}
    _set = {1, 4, 7}
    tup = (1,2)

    print(x, y, b, s)
    print(list)
    print(dict)
    print(_set)
    print(tup)

def IOops():
    file = open('myfile.txt', 'a')
    file.write('000')
    file.close()
    with open('myfile.txt', 'a') as myFile:
        myFile.write('444')

def f1():
    print('f1')
    return False

def f2():
    print('f2')
    return True


def comparisonOperators():
    #b1 = f1()
    #b2 = f2()
    #print(f2() or f1())
    print(1 < 2 < 0)

comparisonOperators()