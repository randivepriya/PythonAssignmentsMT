#Question8:
#Define a function max() that takes two numbers as arguments and returns the largest of them.

def max_of_two (a, b):
    if a>b:
       return a
    elif b>a:
       return b
    else:
       return 0

a=raw_input("Enter First Number ")
b=raw_input("Enter Second Number ")
result=max_of_two(a,b)
print "Maximum Number : ",result


"""
Output:
$python ass8.py
Enter First Number 10
Enter Second Number 58
Maximum Number :  58
$ python ass8.py
Enter First Number 84
Enter Second Number 20
Maximum Number :  84
"""

