# 18. Write a Python program to check whether a given string is number or not using Lambda.

is_number= lambda string: True if string.isdigit() else False


print(is_number('12'))