#Question:
#Define a function that can accept two strings as input and concatenate them and
#then print it in console.

import sys

def concat(string1,string2):
    output=string1+string2
    return output

string1=sys.argv[1]
string2=sys.argv[2]

result=concat(string1,string2)
print result

"""
Output:
$ python ass5.py Priya Randive
PriyaRandive
"""
