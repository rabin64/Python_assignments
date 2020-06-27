def product_list(list):
   product = 1
   for x in list:
       product *= x
   return product
lst=[]
size=int(input("enter the number of a item list: "))
for i in range(size):
    items=int(input("enter the list values to be added: "))
    lst.append(items)

print(product_list(lst))