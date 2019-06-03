def luhn(cardNumber):
    numbers = [int(c) for c in cardNumber]
    numbers1 = (2*x for x in numbers[0::2])
    numbers11 = (x - 9 if x > 9 else x for x in numbers1)
    numbers2 = numbers[1::2]
    checksum = sum(numbers11) + sum(numbers2)
    return checksum % 10 == 0
    pass

cn = '4561261212345467'
print(luhn(cn))
