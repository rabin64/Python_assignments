# 8. Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique_list(given_list):
    result = list(set(given_list))
    return result
lst=[]
a=int(input('enter the size of list:'))
for i in range(0,a):
    i=input("enter the list items:")
    lst.append(i)

print(f'Sample_list: {lst}')

new_list=[]
b=int(input('enter the size of list:'))
for items in range(0,b):
    items=input("enter the list items:")
    lst.append(items)
print(f'Unique List: {unique_list(new_list)}')