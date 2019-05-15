def add(n1, n2):
    print(n1 + n2)

def f1():
    try:
        a = 5
        b = input('b = ')
        add(a , b)
    except TypeError:
        print('type error!')
    except:
        print('any error!')
    else:
        print('All is good')
    finally:
        print('I always run!')


def ask_for_int():
    while True:
        try:
            result = int(input('Enter number: '))
        except:
            print('This is not a number!')
            continue
        else:#means no exception
            print('Thanks!')
            break
        #finally:
            #print('I always run hehehe')

#ask_for_int()

def func1():
    func2()

def func2():
    func3()

def func3():
    raise Exception('ex')

try:
    func1()
except Exception:
    print('Exception processed')