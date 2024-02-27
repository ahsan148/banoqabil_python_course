#Question 7
#Write a program that takes user input for their age and prints a message addressing their age group (e.g., "Teenager," "Adult"). Explore user interaction and conditional statements in Python.

age = int(input('Please enter a persons age.'))

if age >= 0 and age <= 12:
    print("Child")

elif age >= 13 and age <= 19:
    print("Teen")

else:
    print("Adult")
    print(age)
