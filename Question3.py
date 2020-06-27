#3. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
a= input("enter a string:")
print(type(a))
f_letter=a[0]
a = a.replace(f_letter,'$')
a = f_letter + a[1:]
print(a)