# 16. Write a Python program to square and cube every number in a given list of integers using Lambda.
lst=[]
a=int(input('enter the size of list:'))
for i in range(0,a):
    i=int(input("enter the list items:"))
    lst.append(i)

print(f'The given list: {lst}')
lambda_square_list = map(lambda x: x ** 2, lst)
lambda_cube_list = map(lambda x: x ** 3, lst)

print(f'The squared list: {list(lambda_square_list)} ')
print(f'The cubed list: {list(lambda_cube_list)} ')
