#write a python program that
#opens reads a text file named sample.txt
#Handles errors gracefully if the file does not exit
from seaborn import ecdfplot

try:
   file1=open('sample.txt','r')
   read_file=file1.read()
   print("Reading file content:\n",read_file)
   file1.close()

except FileNotFoundError:
    print("The file 'sample.txt' not found")

