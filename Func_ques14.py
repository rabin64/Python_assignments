# 14. Write a Python program to sort a list of dictionaries using Lambda.
list_dict = [{'name': 'rabin', 'last_name': 'shrestha','id':1}, {'name':'saroz', 'last_name':'podel','id':2}, {'name':'rupace', 'last_name':'pandit','id':3}, {'name':'sakchhyam', 'last_name':'thapa','id':2}]
lambda_sorted_dict = lambda dicts: sorted(dicts, key=lambda x: x['id'])

print(f'Given dicts are: {list_dict}')
print(f'Sorted dicts are: {lambda_sorted_dict(list_dict)}')