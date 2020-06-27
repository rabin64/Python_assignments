#14. Write a Python function to create the HTML string with tags around the word(s).

def add_tags(tag, word):
	return "<%s>%s</%s>" % (tag, word, tag)

tag=input("enter the HTML tag: ")
word= input("Enter the wordinside tag:")

print(add_tags(tag,word))
