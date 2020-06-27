# 1. Write a Python function to find the Max of three numbers.

def max_threenumbers(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print(f'{num1} is max ')
    elif num2 > num1 and  num2 > num3:
        print(f'{num2} is max ')
    else:
        print(f'{num3} is max ')

max_threenumbers(5,13,1)