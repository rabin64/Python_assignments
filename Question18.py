def largest_in_list(digit_list):
   largest_number = digit_list[0]
   
   for digit in digit_list:
       if largest_number < digit:
           largest_number = digit
   return largest_number
lst=[]
size=int(input("enter the number of a item list: "))
for i in range(size):
    items=int(input("enter the list values to be added: "))
    lst.append(items)

print(largest_in_list(lst))