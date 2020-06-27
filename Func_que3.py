
# 3. Write a Python function to multiply all the numbers in a list.
from functools import reduce

def product_list(given_list):

    result= reduce(lambda x , y : x * y , given_list)
    return result

result =  product_list([8, 2, 3, -1, 7])
print(f'Product: {result}')