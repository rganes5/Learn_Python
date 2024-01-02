sample_file = open("Wordfile2.txt", "a")
#sample_file = open("Wordfile2.docx", "w")

sample_file.write("Hey I wrote this line from the python code!")
sample_file.write("\nSay my name!")

#Creates a webpage
sample_file = open("index.html", "w")
sample_file.write("<h1>Hello MF!</h1>")

sample_file.close()
