# 22. Write a Python program to remove duplicates from a list.

def remove_duplicates_list(list_items):
   result = list(set(list_items))
   return result
if __name__=="__main__":
    lst = []
    size = int(input("enter the number of a item list: "))
    for i in range(size):
        items = input("enter the list values to be added: ")
        lst.append(items)
    print(remove_duplicates_list(lst))