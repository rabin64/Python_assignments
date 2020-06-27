# 23. Write a Python program to check a list is empty or not.

def check_list_is_empty(list_item):
   if  not  list_item:
       return True
   else:
       return False
if __name__=="__main__":
    lst = []
    size = int(input("enter the number of a item list: "))
    for i in range(size):
        items = input("enter the list values to be added: ")
        lst.append(items)
print(check_list_is_empty(lst))