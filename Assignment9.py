#Question 9:
#Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.

def max_of_three(a,b,c):

    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c

print ("Function to find the largest of three numbers")

print ("Enter the first  number")
firstNumber = int(input())

print ("Enter the second  number")
secondNumber = int(input())

print ("Enter the third  number")
thirdNumber = int(input())

print "Maximum of three: ", max_of_three(firstNumber,secondNumber,thirdNumber)

"""
Output:
python ass9.py
Function to find the largest of three numbers
Enter the first  number
89
Enter the second  number
297
Enter the third  number
40
Maximum of three:  297

"""

