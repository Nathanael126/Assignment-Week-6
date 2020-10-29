# Create variable and create/open files
Counter = 0
File = open("Assignment 6 Book (Beowulf An Anglo-Saxon Epic Poem by J. Lesslie Hall).txt", "r", encoding='UTF8')
New_File = open("Assigment 6 Edited Book.txt","w")
Lines = File.readlines()

# Writes the new file
for a in Lines:
    Counter += 1
    x = "Line:"+str(Counter)+")"+a
    New_File.write(x)