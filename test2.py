'''
myapi.py 
- simple program to demo using a web API with requests Python module
- secondary function to demo how to Enter out received data to an HTML file 
'''

import requests
import json
import pprint

# Find APIs at - https://apilist.fun/
# some will require an API key, boo hiss!

# cool geo example
# https://geo-info.co/?ref=apilist.fun
# example - https://geo-info.co/43.65,-79.40

# cool funny example
# https://funtranslations.com/api/chef
# https://api.funtranslations.com/translate/chef.json?text=I%20like%20upper%20canada%20college

# For any indentation errors, make sure there are no tabs (\t) by doing 
# a full replace of \t with 4 actual spaces

#                                           *   MENU SYSTEM *
print ("Hello! Welcome to THE NHL STATS OUTPUT MACHINE! \n ")
print ("Here is the selection that you can choose from. \n ")

print (" Enter 0 for Connor McDavid. \n")
print (" Enter 1 for Claude Giroux. \n")
print (" Enter 2 for Nikita Kucherov. \n")
print (" Enter 3 for Evgeni Malkin. \n")
print (" Enter 4 for Nathan MacKinnon. \n")
print (" Enter 5 for Taylor Hall. \n")
print (" Enter 6 for Anze Kopitar. \n")
print (" Enter 7 for Phil Kessel. \n")
print (" Enter 8 for Blake Wheeler. \n")
ItemChosen = int(input("Please make your selection. \n"))



def writeHTML(data):
    myfile = open("myapi.html","w")
    myfile.write("<h1> 2017-2018 NHL SEASON STATS </h1>")
    myfile.write("<h3> THIS INCLUDES ALL THE PLAYERS IN THE NHL WITH THEIR PERSONAL STATS AND INFORMATION </h1>")
    myfile.write(data)
    myfile.close()

def main():

    # Call to Database

    response = requests.get("http://www.nhl.com/stats/rest/skaters?isAggregate=false&reportType=basic&isGame=false&reportName=skatersummary&sort=[{%22property%22:%22points%22,%22direction%22:%22DESC%22},{%22property%22:%22goals%22,%22direction%22:%22DESC%22},{%22property%22:%22assists%22,%22direction%22:%22DESC%22}]&cayenneExp=gameTypeId=2%20and%20seasonId%3E=20172018%20and%20seasonId%3C=20172018")

    
    data = response.content # response comes in as byte data type
    data_as_str = data.decode()    # decode to str
    #writeHTML(data_as_str)  # call function to write string data to HTML file

    datajson = response.json()
                                    #*********************** MCDAVID ***********************

    if ItemChosen == 0:

                                    #*********************** STATS ***********************

        print (" Now please choose one of the following stats/personal info. \n")

        print (" Enter 1 for Games Played (GP). \n")

        print (" Enter 2 for Goals (G). \n")

        print (" Enter 3 for Assists (A). \n")

        print (" Enter 4 for Points (P). \n")
        
        print (" Enter 5 for Points Per Game (PPG). \n")

        print (" Enter 6 for Game Winning Goals (GWG). \n")

        print (" Enter 7 for Plus/Minus (+/-). \n")

        print (" Enter 8 for Penalty Minutes (PM). \n")

        print (" Enter 9 for Power Play Goals (PPG). \n")
                    
        print (" Enter 10 for Power Play Points (PPP). \n")
                        
        print (" Enter 11 for Shorthanded Goals. \n")
                            
        print (" Enter 12 for Shorthanded Points. \n")

        print (" Enter 13 for Faceoff Percentage (Faceoff%). \n")
           
        print (" Enter 14 for Shifts Per Game and Time on Ice Per Game. \n")

        print (" Enter 15 for Shots and Shooting Percentage. \n")

        print (" Enter 16 for Birth Date, City, State/Province/Territory, Country, Nationality. \n")

        print (" Enter 17 for Draft Overall Pick Number, Round Number, Draft Year. \n")

        print (" Enter 18 for Height, Weight, Id number, Status (1 = Yes, 0 = No). \n")

        print (" Enter 19 for Position, Shoots/Catches, Team. \n")

        StatChosen = int(input("Please make your selection. \n"))

    if StatChosen == 1:

        GPdata = datajson ['data'][0]['gamesPlayed']
        print ("\n Connor McDavid's Games Played in 2017-2018 was " + str(GPdata) + "\n")
    

    elif StatChosen == 2:
        Gdata = datajson ['data'][0]['goals']
        print ("\n Connor McDavid's Goals in 2017-2018 was " + str(Gdata) + "\n")

main()


