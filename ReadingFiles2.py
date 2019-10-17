# Author: Kalen
# Upper Canada College


print ("This program will read your favourite sports")

a = open("fileinfo.txt", "r")

print(a.read(20))
print ("")
a = open("fileinfo.txt", "r")
print(a.read())

input("Press ENTER to quit the program")