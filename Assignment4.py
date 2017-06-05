#Question: Write a Python program to count the number of lines in a text file.

file_object = open("Assignment1.py", "r+")

count = 0

for line in file_object:
    count=count +1

file_object.close()
print "No.of line in file: ",count

'''
Output:
No.of line in file:  19
'''


"""
import sys
file_object=open(sys.argv[1], "r+")
"""
