# 33. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys

num =int(input("Enter a number:")) #enter 15

dict = {}
for index in range(1, num+1):
    dict[index] = index ** 2
print(dict)