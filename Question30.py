# 30. Write a Python script to check whether a given key already exists in a dictionary.

test_key = 15
main_dict = {1: 3, 2: 4, 3: 5, 4: 6, 5: 7}
count = 0
for key in main_dict:
    if key == test_key:
        count = 1

if count == 1:
    print('key exists.')
else:
    print("key doesn't exist.")