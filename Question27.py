# 27. Write a Python program to replace the last element in a list with another list.

def replace_last_element(list1, list2):
    result = list1[:-1] + list2
    return result
list1=[]
list2=[]
list1_len=int(input("enter the size of list 1"))

for i in range(list1_len):
    items=input("enter the items:")
    list1.append(items)

list2_len=int(input("enter the size of list 2:"))

for i in range(list2_len):
    items=input("enter the list2 items:")
    list2.append(items)

res = replace_last_element(list1, list2)
print(f'List1: {list1}\nList2: {list2}\nResult: {res}')
