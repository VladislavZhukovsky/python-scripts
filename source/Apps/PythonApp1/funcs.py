
def func_1(name = 'man'):
    '''
    prints Hello!
    '''
    print('Hello ' + name)

def string_contains(s, fragment):
    return fragment in s.lower()

def pig_latin(word):
    if (word[0] in 'aeiouy'):
        result = word + 'ay'
    else:
        result = word[1:] + word[0] + 'ay'
    return result

def my_sum(n, *numbers): #tuple
    print(type(numbers))
    return n + sum(numbers) * 0.05

#print(my_sum(10000, 60))

def dict_func(**kwargs): #dict
    print(type(kwargs))
    print(kwargs)

#dict_func(k1 = '11', k2 = '22')

def count_primes(num):
    primes = [2]
    for a in range(3,num+1,2):
        aIsPrime = True;
        for b in primes:
            if a % b == 0:
                aIsPrime = False
                break
        if aIsPrime:
            primes.append(a)
    return len(primes)

print(count_primes(100))