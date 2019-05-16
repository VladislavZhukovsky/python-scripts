def uppers_and_lowers(s):
    uppers = list(filter(lambda c: c.isupper(), s))
    lowers = list(filter(lambda c: c.islower(), s))
    return (len(uppers), len(lowers))

#print(uppers_and_lowers('Hello Mr. Rogers, how are you this fine Tuesday?'))

def unique_list(l):
    s = set(l)
    return list(s)

#l = [1,1,1,1,2,2,3,3,3,3,4,5]
#uniques = unique_list(l)
#print(type(uniques))
#print(uniques)

def ispangram(s):
    
    sset = set(filter(lambda c: c.isalpha(), s.lower()))
    import string
    alphabet = set(string.ascii_lowercase)
    return alphabet.issubset(sset)

s = "The quick brown fox jumps over the lazy dog"
print(ispangram(s))