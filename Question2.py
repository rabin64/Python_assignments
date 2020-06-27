a = input("enter a string:")
print(type(a))

if len(a) < 2:
        print("empty string")
else:
        print(a[0:2] + a[-2:])