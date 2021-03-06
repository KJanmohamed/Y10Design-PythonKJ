# Author: Kalen Janmohamed
# For: Mr. Jugoon
# Date: October 25 2019

import requests
import json
import pprint

#                                           *--------------  MENU SYSTEM -----------------*

print ("Hello! Welcome to THE NHL STATS OUTPUT MACHINE! \n ")
print ("Here is the selection that you can choose from. \n ")

print (" Enter 1 for Connor McDavid. \n")
print (" Enter 2 for Mitch Marner. \n")
print (" Enter 3 for Sidney Crosby. \n")
print (" Enter 4 for Auston Matthews. \n")
print (" Enter 5 for Nathan MacKinnon. \n")
print (" Enter 6 for Nikita Kucherov. \n")
print (" Enter 7 for Alexander Ovechkin. \n")
print (" Enter 8 for Patrick Kane. \n")
print (" Enter 9 for William Nylander. \n")
print (" Enter 10 for John Tavares. \n")
print (" Enter 11 for Claude Giroux. \n")
print (" Enter 12 for Evgeni Malkin. \n")
print (" Enter 13 for Taylor Hall. \n")
print (" Enter 14 for Anze Kopitar. \n")
print (" Enter 15 for Phil Kessel. \n")
print (" Enter 16 for Blake Wheeler. \n")
print (" Enter 17 for Steven Stamkos. \n")
print (" Enter 18 for Brad Marchand. \n")
print (" Enter 19 for Matthew Barzal. \n")
print (" Enter 20 for Jakub Vorácek. \n")

#                                           *--------------  ITEM CHOSEN VARIABLE -----------------*

ItemChosen = int(input("Please make your selection - if not a valid answer the program will not continue. \n"))


#                                           *--------------  HTML FILE -----------------*

'''
def writeHTML(data):
    myfile = open("myapi.html","w")
    myfile.write("<h1> 2017-2018 NHL SEASON STATS </h1>")
    myfile.write("<h3> THIS INCLUDES ALL THE PLAYERS IN THE NHL WITH THEIR PERSONAL STATS AND INFORMATION </h1>")
    myfile.write(data)
    myfile.close()
'''

def writeHTML(data):
    myfile = open("myapi.html","w") # use "a" to "append"    
    myfile.write("""
    <html>

      <head>
        <title> MY PAGE </title>
      </head>

      <body>
        <font size="3" color="red">This is some text!</font>
        <font size="2" color="blue">This is some text!</font>
        <font face="verdana" color="green">This is some text!</font>
        <h1>Welcome to My Soccer Home Page</h1>

        <p>Go to <a href='https://apilist.fun/api/the-sports-db'>The Sports DB</a> for API Info.</p>

        <h1 style="background-color:DodgerBlue;">Here is player you requested</h1>

        <p>The Data you requested is: """+ data+"""</p>

        <p style="font-family:verdana">This is a paragraph.</p>

        <p style="font-family:'Courier New'">This is another paragraph.</p>

      </body>

    </html>""")

    myfile.close()

def main():

#                                           *--------------  CALL TO API -----------------*

    response = requests.get("http://www.nhl.com/stats/rest/skaters?isAggregate=false&reportType=basic&isGame=false&reportName=skatersummary&sort=[{%22property%22:%22points%22,%22direction%22:%22DESC%22},{%22property%22:%22goals%22,%22direction%22:%22DESC%22},{%22property%22:%22assists%22,%22direction%22:%22DESC%22}]&cayenneExp=gameTypeId=2%20and%20seasonId%3E=20172018%20and%20seasonId%3C=20172018")
    data = response.content # response comes in as byte data type
    data_as_str = data.decode()    # decode to str
    #writeHTML(data_as_str)  # call function to write string data to HTML file

    datajson = response.json()

                                    #*********************** MCDAVID ***********************

    if ItemChosen == 1:

                                    #*********************** OPTIONS ***********************

        print (" Now please choose one of the following stats/personal info. \n")

        print (" Enter 1 for Games Played (GP). \n")

        print (" Enter 2 for Goals (G), Assists (A), Points (P) and Points Per Game (PPG). \n")

        print (" Enter 3 for Game Winning Goals (GWG). \n")

        print (" Enter 4 for Plus/Minus (+/-). \n")

        print (" Enter 5 for Penalty Minutes (PM). \n")

        print (" Enter 6 for Power Play Goals (PPG) and Power Play Points (PPP). \n")
                        
        print (" Enter 7 for Shorthanded Goals (SH) and Shorthanded Points (SP). \n")

        print (" Enter 8 for Faceoff Percentage (Faceoff%), Shots (S) and Shooting Percentage (S%). \n")
           
        print (" Enter 9 for Shifts Per Game and Time on Ice Per Game. \n")

        print (" Enter 10 for Birth Date, City, State/Province/Territory, Country, Nationality. \n")

        print (" Enter 11 for Draft Overall Pick Number, Round Number, Draft Year. \n")

        print (" Enter 12 for Height and Weight. \n")

        print (" Enter 13 for Position, Shoots/Catches, Team. \n")

        #                                           *--------------  STAT CHOSEN VARIABLE -----------------*

        StatChosen = int(input("Please make your selection - if not a valid answer the program will not continue. \n"))

        #                                           *--------------  GAMES PLAYED -----------------*

        if StatChosen == 1:

            CMGPdata = datajson ['data'][0]['gamesPlayed']
            print ("\n Connor McDavid had " + str(CMGPdata) + " Games Played in 2017-2018. \n")

            #######ADD THIS IN #########
            writeHTML(str(CMGPdata))

main()