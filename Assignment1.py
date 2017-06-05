#Question1 : Write a python script for creating directory,displaying its contents.
import os

os.mkdir('Assignment1')
os.chdir('Assignment1')

os.system('touch a.txt')
os.system('touch a11.txt')
print os.listdir(os.curdir)
print os.listdir('..')


'''

Output:
['a11.txt', 'a.txt']
['.pydevproject', 'Assignment1', 'ass1.py', '.project']

'''
