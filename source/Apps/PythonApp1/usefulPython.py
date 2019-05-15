def rangefunc():
    r = list(range(1,8,2))
    print(r)

def enumerateFunc():
    word = 'abcde'
    for index, letter in enumerate(word):
        print(f'{index}-{letter}')

def zipFunc():
    l1 = [1,2,3]
    l2 = ['a', 'b', 'c']
    l3 = [True, False, True]
    zp = zip(l1, l2, l3)
    print(zp)
    for item in zp:
        print(item)
    list(zp)
    
def shuffleFunc():
    from random import shuffle
    myList = [1,2,3,4]
    shuffle(myList)
    print(myList)

def inputFunc():
    inpt = input("What's your name? ")
    print(f'Hello {inpt}!')