# Here is a program to show how to use "if - elif - else"
# The hash-tag is used to show that these are comments
# This means that the computer will not look at these lines
# Author: Kalen Janmohamed
# Upper Canada College

# Put down some options for the user to choose from...

print("1. When's your next hockey game?")
print("2. What is your schedule for today?")
print("3. What homework do I have to complete?")
print(" ")
print("Choose one of the options above")

mood = int(input("Tell me what you would like to know? \n"))

if mood == 1:
    print("On Wednesday against Duffield, they have a 3-0-1 record.")
elif mood == 2:
    print ("You are going to have coding at 8:30, then have assembly at 10:05, you then traval to physics from 10:50 to 12:20. You then have lunch until 1:10 and u have to change for gym. After gym at 2:00 you have chemistry and finally at 4:00 you have soccer practice.")
elif mood == 3:
    print ("You have English, French, Math and Geography homework.")
else:
    print ("This is not a valid choice")
    print ("Hope you have a great day anyway!")


# This is a way to gracefuuly exit the program
input("Press ENTER to quit the program")
