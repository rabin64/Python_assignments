
#Write a Python program to sum all the items in a list.
def add(items):
    sum = 0
    for x in items:
        sum += x
    return sum

lst=[]
size=int(input("enter the number of a item list: "))
for i in range(size):
    items=int(input("enter the list values to be added: "))
    lst.append(items)

print(sum(lst))