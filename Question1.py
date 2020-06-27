#1. Write a Python program to count the number of characters (character frequency) in a string. Sample String : google.com'

def input_stringy(str1):
    dict = {}
    print(type(dict))
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    print(keys)
    return dict
a=input_stringy('google.com')
print(a)




