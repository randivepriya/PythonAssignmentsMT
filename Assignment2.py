#Question: 
#Write a python script which will display system name ,node name and release details of current system.

import os

all_info=os.uname()

print "System Name: ",all_info[0]
print "Node Name: ",all_info[1]
print "Release: ",all_info[2]

'''
Output:
System Name:  Linux
Node Name:  python-server-kt
Release:  3.10.0-514.21.1.el7.x86_64
'''

