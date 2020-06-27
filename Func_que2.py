# 2. Write a Python function to sum all the numbers in a list.
from functools import reduce
def sum_list(given_list):
    result= reduce(lambda x , y : x + y , given_list)
    return result

res =  sum_list([1,2,3,4,5,6])
print(f'result: {res}')