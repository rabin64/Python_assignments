# 11. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and print the result.

first_lambda_function = lambda x: x + 15
second_lambda_function = lambda x, y: x * y

value1=int(input("enter value 1:"))
value2=int(input("enter value 2:"))
print(first_lambda_function(value1))
print(second_lambda_function(value1,value2))