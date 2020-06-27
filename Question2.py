#2. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.
a = input("enter a string:")
print(type(a))

if len(a) < 2:
        print("empty string")
else:
        print(a[0:2] + a[-2:])