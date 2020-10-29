# Import book and create dictionary for words
Book = open("Assignment 5 Book (Alice's Adventures in Wonderland by Lewis Carroll).txt","r" ,encoding='utf8')
words = {}

# Finding Hapaxes
for a in Book:
    for b in a.split():
        if b in words:
            words[b] += 1
        else:
            words[b] = 1

# Print Hapaxes
print("All hapax legomenons: ")
for a in words:
    if words[a] == 1:
        print(a)