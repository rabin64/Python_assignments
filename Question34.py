# 34. Write a Python script to merge two Python dictionaries.


dict1 = {'1': 1, '2': 2}
dict2 = {'2': 3, '3': 4}
d = dict1.copy()
d.update(dict2)
print(d)