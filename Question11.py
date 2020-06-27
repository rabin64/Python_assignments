#11. Write a Python program to count the occurrences
# of each word in a given	 sentence

def word_count(str):
    counts = dict()
    print(type(counts))
    words = str.split()

    for n in words:
        if n in counts:
            counts[n] += 1
        else:
            counts[n] = 1

    return counts
a=input("enter a sentence:")
print(word_count(a))