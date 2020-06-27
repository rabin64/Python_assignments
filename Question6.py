#6.	Write a Python program to find the first appearance of
# the substring 'not' and	 'poor' from a given string,
# if 'not' follows the 'poor', replace the whole 'not'...'poor'
# substring with 'good'. Return the resulting string.

def sentence(a):
    snot = a.find('not')
    spoor = a.find('poor')

    if spoor > snot and snot > 0 and spoor > 0:
        a = a.replace(a[snot:(spoor+4) ] , 'good')
        return a
    else:
        return a

input_string= input("enter a sentence:")
print(sentence(input_string))

