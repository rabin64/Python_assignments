# 13. Write a Python program to sort a list of tuples using Lambda.
lambda_sort_tuples = lambda tuples : sorted(tuples , key=lambda tup: tup[-1:])
given_list = [(1,2),(3,2),(1,4),(7,0)]

print(f'The given tuples are: {given_list}')
print(f'The sorted tuples are: {lambda_sort_tuples(given_list)}')