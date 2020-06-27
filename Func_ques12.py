# 12. Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.
def multiply(x):
    return lambda unknown_given_num : x * unknown_given_num

result = multiply(4)
print(f'The result is: {result(5)}')