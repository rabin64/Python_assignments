def string_count(string_list):
   count = 0
   for string in string_list:
       if len(string) >= 2:
           if string[0] == string[-1]:
               count += 1
   return count
lst=[]
size=int(input("enter the number of a item list: "))
for i in range(size):
    items=input("enter the list values to be added: ")
    lst.append(items)
print(string_count(lst))