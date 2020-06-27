#12.	Write a Python script that takes input from the user
# and displays that input back in upper and lower cases

def upper_lower(str):
    print("upper case:",str.upper())
    print("lower case:",str.lower())
    return 0

userinput=input("enter a string:")
upper_lower(userinput)