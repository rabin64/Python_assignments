# 17. Write a Python program to find if a given string starts with a given character using Lambda.
string_starts_with = lambda char, string: True if string.startswith(char) else False

starting_char=input("enter a character to check:")
given_string=input("enter the string:")
print(string_starts_with(starting_char,given_string))