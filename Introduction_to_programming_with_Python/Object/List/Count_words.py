def count_words(sen):
    """"sen is the sentance representing a string 
    representing how many words are there in s"""
    """word = A sequence of character between spaces. """
    L = sen.split(' ')
    return len(L)

# print(count_words("Hello it's me"))

L = [9,6,0,3]
L.append(5)
print(L)
a = sorted(L)
print(a)
print(L)
b = L.sort()
print(b)
print(L)
L.reverse()
print(L)
