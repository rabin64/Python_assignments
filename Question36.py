# 36. Write a Python program to sum all the items in a dictionary.
dict1 =  {1:1, 2:2, 3:3, 4:4}
sum_items = 0
for value in dict1.values():
    sum_items+=value
print(sum_items)