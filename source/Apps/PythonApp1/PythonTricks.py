def mergeDicts():
    x = {'a': 1, 'b': 2}
    y = {'c': 3, 'b': 4}
    z = dict(x, **y)
    z = {**x, **y}
    print(z)

def testMultipleFlags():
    x, y, z = 0, 0.0, 0
    if 1 in (x, y, z): #only for 1s
        print('passed')
    if x or y or z: #false only for zeros
        print('passed')
    if any([x, y, z]):
        print('passed')

def dictDefaultValue():
    d = { 123: 'Alice', 456: 'Bob' }
    print(d[123])
    print(d[456])
    print(d.get(789, 'there'))

def namedTupleAsClass():
    from collections import namedtuple
    Car = namedtuple('Car', 'color mileage')
    car1 = Car('Merc', 100)
    print(car1.color)
    print(car1.mileage)

def importThis():
    import this