# 28. Write a Python script to add a key to a dictionary.

def add_key(item):
   main_dict =  {0: 1, 1: 2}
   main_dict.update(item)
   print(main_dict)


add_key({2:3})