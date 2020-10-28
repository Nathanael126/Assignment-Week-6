Book = open("Assignment 7 Book (Frankenstein; Or, The Modern Prometheus by Mary Wollstonecraft Shelley).txt","r" ,encoding='utf8')
Word_Length = 0
counter = 0
for a in Book:
    for b in a.split():
        counter += 1
        Word_Length += len(b)
print("Average length of words:",Word_Length/counter)