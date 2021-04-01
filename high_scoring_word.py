#Given a string of words, you need to find the highest scoring word.

#Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

#You need to return the highest scoring word as a string.

#If two words score the same, return the word that appears earliest in the original string.

#All letters will be lowercase and all inputs will be valid.


def high(x):
    arr, numArr = x.split(' '), []
    
    for val in arr:
        num = 0
        letters = list(val)
        for word in letters:
            num += ord(word) - 96
        numArr.append(num)
    return arr[numArr.index(max(numArr))]

print(high('where in the world is carmen san diego'))
