# 15. Write a Python program to filter a list of integers using Lambda.


lambda_integer_filter = lambda list: filter(lambda y: y > 2, list)

lst=[]
a=int(input('enter the size of list:'))
for i in range(0,a):
    i=int(input("enter the list items:"))
    lst.append(i)

print(f'The given list: {lst}')
print(f'The filtered list having number greater than 2: {list(lambda_integer_filter(lst))}')