a= input("enter a string:")
print(type(a))
f_letter=a[0]
a = a.replace(f_letter,'$')
a = f_letter + a[1:]
print(a)