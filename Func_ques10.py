# 10. Write a Python program to print the even numbers from a given list.
def even_list(given_list):
    result = [n for n in given_list if n % 2==0]
    return result

lst=[]
a=int(input('enter the size of list:'))
for i in range(0,a):
    i=int(input("enter the integer list items:"))
    lst.append(i)


print(even_list(lst))