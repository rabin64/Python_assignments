# 6. Write a Python function to check whether a number is in a given range.
def check_range(number,range_from, range_to):
    if number in range(range_from, range_to):
        return True
    else:
        return False
number=int(input("enter a number to check:"))
range_from=int(input("enter a range's initial number:"))
range_to=int(input("enter a range's final number:"))
print(check_range(number, range_from, range_to))