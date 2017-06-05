#Question:
#Write a program that takes inputs from user their name and their age. 
#And display the year in which they will turn 100 years old.

name = raw_input("Enter your Name ")
age = int(raw_input("Enter your age "))
current_age = 2017 - age
year_century= current_age+100

print(name + " will be 100 years old in the year ",year_century)


"""
Output:
Enter your Name Priya
Enter your age 23
('Priya will be 100 years old in the year ', 2094)
"""

