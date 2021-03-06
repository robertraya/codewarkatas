##The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.##

##What if the string is empty? Then the result should be empty object literal, {}. ##

def count(string):
    count = dict()
    letters = list(string)
    
    for i in letters:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count
    
    
string = 'aba'

count(string)
