# 26. Write a Python program to insert a given string at the beginning of all items in a list.

def insert_string(list_items, string):
    result_list = []
    for item in list_items:
        item = string + str(item)
        result_list.append(item)
    return result_list



main_list = [1, 2, 3]
string = input("enter a string:")
res = insert_string(main_list, string)
print("List: %s  String: %s Result:",main_list,string,res)