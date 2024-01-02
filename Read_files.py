# open("Wordfile.docx", "w")  #Write
# open("Wordfile.docx", "a")  #Append

sample_file = open("Wordfile2.txt", "r")  #Readmode
print(sample_file.readable()) #Checks whether readable or not

print(sample_file.readline()) #reads line by line - 1st line
print(sample_file.readlines())

# OR

#for data in sample_file.readlines():
 #   print(data)

# ALWAYS CLOSE EVERY FILE THAT WE OPEN OR READ
sample_file.close()