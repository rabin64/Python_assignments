#8.	Write a Python program to remove the nth index character
# from a nonempty string

def remove_char(str, n):
    first_part = str[:n]
    last_part = str[n + 1:]
    return first_part + last_part

a=input("enter a string:")
b=int(input("enter the index:"))
print(remove_char(a, 0))

