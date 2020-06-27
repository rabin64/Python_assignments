# 41. Write a Python program to convert a tuple to a string.

def convertTuple(example):
    str = ''.join(example)
    return str
sampletuple = ('r', 'a', 'b', 'i', 'n')
str = convertTuple(sampletuple)
print(str)
print(type(str))