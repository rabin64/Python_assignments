# 37. Write a Python program to multiply all the items in a dictionary.

dict1 =  {1:1, 2:2, 3:3, 4:4}
product_items = 1
for value in dict1.values():
    product_items *= value
print(product_items)