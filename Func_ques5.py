
# 5. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)

given_num=int(input("Enter a number:"))
print(factorial(given_num))