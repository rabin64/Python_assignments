#4. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
def swap(a, b):
  new_a = b[:2] + a[2:]
  new_b = a[:2] + b[2:]

  return new_a + ' ' + new_b

f_str=input("Enter a first string:")
s_str=input("enter a aecond string:")

print(swap(f_str, s_str))
