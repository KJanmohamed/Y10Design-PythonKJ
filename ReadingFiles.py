# Author: Kalen
# Upper Canada College

print ("This will write your favourite sport to a file")

sport = str(input("What are your favourite sports?"))

f = open("fileinfo.txt", "a")
f.write ("\n" + sport + "\n")
f.close()

f = open("fileinfo.txt", "r")
print (f.read())

input("Press ENTER to quit the program")