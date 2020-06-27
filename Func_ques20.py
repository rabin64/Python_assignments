# 20. Write a Python program to find intersection of two given arrays using Lambda.
list1 = [1,2,3,4,5,6]
list2 = [3,4,6,5,2]

intersection = lambda list1, list2: [x for x in list1 if x in list2]

print(intersection(list1, list2))