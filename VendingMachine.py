#This program simulates a vending machine
#Authors: Kalen Janmohamed
#Date: September 20 2019 - September 28 2019
#Upper Canada College

print (" \n")
print ("Hello! Welcome to the Worlds cheapest vending machine! \n ")
print ("Here is the selection that you can choose from. \n ")

print(" 				ROW 1 - DRINK ")

print (" 1. Coke 	    2. Sprite 	    3. Crush 	    4. Peace Tea - Mango")
print (" $1.50 		    $1.50	    $2.00	    $2.25	\n ")

print(" 				ROW 2 - FOOD ")

print (" 5. Doritos 	    6. Kit Kat 	    7. Crunchie  	    8. Welch's")
print (" $1.00 		    $1.00	    $1.00	    $1.50	\n ")

#VARIABLES

ItemChosen = int(input("Please make your selection. \n"))

Money = 0.00

Left = 0.00

Price1 = 1.50

Price2 = 1.50

Price3 = 2.00

Price4 = 2.25

Price5 = 1.00

Price6 = 1.00

Price7 = 1.00

Price8 = 1.50

#*********************** COKE - 1.50 ***********************

if ItemChosen == 1:
	Money = float(input("Selected: Coke. Please insert $1.50. \n"))
	if Money == 1.50:
		print("Coke dispensed. \n")
	elif Money < 1.50:
		print("Insufficient Funds. \n")
		print("Your Purchase Has Been Canceled And You Have Lost $"+str(Money)+ ". \n")
	elif Money > 1.50:
		Left = Money - 1.50
		print("You have lost $"+str(Left)+" since the Coke only costed $"+str(Price1)+". \n")
		print("Have A Splendid Day! :) :) :) :) \n")
 
#*********************** SPRITE  - 1.50 ***********************

elif ItemChosen == 2:
	Money = float(input("Selected: Sprite. Please insert $1.50. \n"))
	if Money == 1.50:
		print("Sprite dispensed. \n")
	elif Money < 1.50:
		print("Insufficient Funds. \n")
		print("Your Purchase Has Been Canceled And You Have Lost $"+str(Money)+". \n")
	elif Money > 1.50:
		Left = Money - 1.50
		print("You have lost $"+str(Left)+" since the Sprite only costed $"+str(Price2)+". \n")
		print("Have A Splendid Day! :) :) :) :) \n")

#*********************** Crush - 2.00 ***********************

elif ItemChosen == 3:
	Money = float(input("Selected: Crush. Please insert $2.00. \n"))
	if Money == 2.00:
		print("Crush dispensed. \n") 
	elif Money < 2.00:
		print("Insufficient Funds. \n")
		print("Your Purchase Has Been Canceled And You Have Lost $"+str(Money)+". \n")
	elif Money > 2.00:
		Left = Money - 2.00
		print("You have lost $"+str(Left)+" since the Crush only costed $"+str(Price3)+". \n")
		print("Have A Splendid Day! :) :) :) :) \n")

#*********************** Peace Tea - Mango - 2.25 ***********************

elif ItemChosen == 4:
	Money = float(input("Selected: Peace Tea - Mango. Please insert $2.25. \n"))
	if Money == 2.25:
		print("Peace Tea - Mango dispensed. \n")
	elif Money < 2.25:
		print("Insufficient Funds. \n")
		print("Your Purchase Has Been Canceled And You Have Lost $"+str(Money)+". \n")
	elif Money > 2.25:
		Left = Money - 2.25
		print("You have lost $"+str(Left)+" since the Peace Tea - Mango only costed $"+str(Price4)+". \n")
		print("Have A Splendid Day! :) :) :) :) \n")

#*********************** Doritos - 1.00 ***********************

elif ItemChosen == 5:
	Money = float(input("Selected: Doritos. Please insert $1.00. \n"))
	if Money == 1.00:
		print("Doritos dispensed. \n")
	elif Money < 1.00:
		print("Insufficient Funds. \n")
		print("Your Purchase Has Been Canceled And You Have Lost $"+str(Money)+". \n")
	elif Money > 1.00:
		Left = Money - 1.00
		print("You have lost $"+str(Left)+" since the Doritos only costed $"+str(Price5)+". \n")
		print("Have A Splendid Day! :) :) :) :) \n")

#*********************** Kit Kat - 1.00 ***********************

elif ItemChosen == 6:
	Money = float(input("Selected: Kit Kat. Please insert $1.00. \n"))
	if Money == 1.00:
		print("Kit Kat dispensed. \n")
	elif Money < 1.00:
		print("Insufficient Funds. \n")
		print("Your Purchase Has Been Canceled And You Have Lost $"+str(Money)+". \n")
	elif Money > 1.00:
		Left = Money - 1.00
		print("You have lost $"+str(Left)+" since the Kit Kat only costed $"+str(Price6)+". \n")
		print("Have A Splendid Day! :) :) :) :) \n")

#*********************** Crunchie - 1.00 ***********************

elif ItemChosen == 7:
	Money = float(input("Selected: Crunchie. Please insert $1.00. \n"))
	if Money == 1.00:
		print("Crunchie dispensed. \n")
	elif Money < 1.00:
		print("Insufficient Funds. \n")
		print("Your Purchase Has Been Canceled And You Have Lost $"+str(Money)+". \n")
	elif Money > 1.00:
		Left = Money - 1.00
		print("You have lost $"+str(Left)+" since the Crunchie only costed $"+str(Price7)+". \n")
		print("Have A Splendid Day! :) :) :) :) \n")

#*********************** Welch's - 1.50 ***********************

elif ItemChosen == 8:
	Money = float(input("Selected: Welch's. Please insert $1.50. \n"))
	if Money == 1.50:
		print("Welch's dispensed. \n")
	elif Money < 1.50:
		print("Insufficient Funds. \n")
		print("Your Purchase Has Been Canceled And You Have Lost $"+str(Money)+". \n")
	elif Money > 1.50:
		Left = Money - 1.50
		print("You have lost $"+str(Left)+" since the Welch's only costed $"+str(Price8)+". \n")
		print("Have A Splendid Day! :) :) :) :) \n")

input("Press ENTER to quit the program")



















