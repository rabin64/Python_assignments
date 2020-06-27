# 7. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

def calculate(string):
    uppercase_number = 0
    lowercase_number = 0
    for char in string:
        if char.isupper():
            uppercase_number += 1
        if char.islower():
            lowercase_number += 1
    return(uppercase_number, lowercase_number)
str=input("enter a string:")
uppercase, lowercase = calculate(str)
print(f'Number of uppercase letters: {uppercase}')
print(f'Number of lowercase letters: {lowercase}')