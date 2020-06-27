#9.	Write a Python program to change a given string to a new
# string where the first and last chars have been exchanged

def change(str):
    n=len(str)
    print(n)
    first_char=str[0]
    last_char=str[n-1]
    return last_char+str[1:n-1]+first_char
string = input("Enter a string:")

print(change(string))