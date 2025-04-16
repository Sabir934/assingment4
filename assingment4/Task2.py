#write a python program that:
#1.Takes user input and writes it to file name output.txt
#2.Appends additional data to the same file.
#3.Reads and Display the final content to the files

user_input=input(str("Enter text to write to the file: "))

file1=open('output.txt','w')
write_file1=file1.write(user_input)
print("Data successfully written to output.text\n")
file1.close()

#append additional data to the same file


file1=open('output.txt','a')
append_file1=file1.write("\nLearning file handling in python")
print("Data successfully appended.")
file1.close()

#display the file content using read code

file1=open('output.txt','r')
print("Final content of output.txt")
read_fil1=file1.read()
print(read_fil1)
file1.close()
