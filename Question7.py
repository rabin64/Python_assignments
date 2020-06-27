#7.	Write a Python function that takes a list of words
# and returns the length of the longest one

def find_longest_word(words_list):
    word_len = []
    print(type(word_len))
    for n in words_list:
        word_len.append((len(n), n))


    word_len.sort()

    return print("longest word:",word_len[-1][1] + " and length is :", word_len[-1][0])



#n = input("Enter strings seperated by space: ")


#userlist= n.split()
lst=[]
a=int(input('enter the size of list:'))
for i in range(0,a):
    i=input("enter the strings:")
    lst.append(i)

#print("user list is ", userlist)
find_longest_word(lst)