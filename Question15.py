#Write a Python function to insert a string in the middle of a string.

def insert_sting_middle(str, word):
    n=len(str)
    a=int(n/2)
    return str[:a] + word + str[a:]

a=input("enter a string in which a word is to be insterted:")
b=input("enter a word to be inserted:")
print(insert_sting_middle(a,b))
