"""
Question 11:
Write a program that accepts a sentence and calculate the number of letters and digits.
              Suppose the following input is supplied to the program:
              i/p: Hello Priya 1287
              o/p: LETTERS 10
                   DIGITS 4
"""
given_input = raw_input()
d={"DIGITS":0, "LETTERS":0}
for c in given_input:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass
print "LETTERS", d["LETTERS"]
print "DIGITS", d["DIGITS"]


"""
Output:
$ python Assignment11.py
Priya 2017
LETTERS 5
DIGITS 4
"""

