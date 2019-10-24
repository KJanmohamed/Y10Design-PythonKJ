'''
myapi.py 
- simple program to demo using a web API with requests Python module
- secondary function to demo how to Enter out received data to an HTML file 
'''

import requests
import json
import webbrowser

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


def writeHTML(data1, data2, data3, data4, data5):
    myfile = open("myapi.html","w")

    #The file's location is different for every user
    filename1 = 'file:///Users/kalen.janmohamed/Desktop/Git%20Repo/Y10Design-PythonKJ/myapi.html'

    #Opens the HTML file in a new tab
    webbrowser.open_new_tab(filename1)




                                                            #REQUEST
def main():

    # Call to Database

    response = requests.get("http://www.nhl.com/stats/rest/skaters?isAggregate=false&reportType=basic&isGame=false&reportName=skatersummary&sort=[{%22property%22:%22points%22,%22direction%22:%22DESC%22},{%22property%22:%22goals%22,%22direction%22:%22DESC%22},{%22property%22:%22assists%22,%22direction%22:%22DESC%22}]&cayenneExp=gameTypeId=2%20and%20seasonId%3E=20172018%20and%20seasonId%3C=20172018")

    
    data = response.content # response comes in as byte data type
    data_as_str = data.decode()    # decode to str
    #writeHTML(data_as_str)  # call function to write string data to HTML file

    datajson = response.json()





#                                           *   MENU SYSTEM *
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
ItemChosen = int(input("Please make your selection - if not a valid answer the program will not continue. \n"))









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

        StatChosen = int(input("Please make your selection - if not a valid answer the program will not continue. \n"))

        if StatChosen == 1:
            CMGPdata = datajson ['data'][0]['gamesPlayed']
            print ("\n Connor McDavid had " + str(CMGPdata) + " Games Played in 2017-2018. \n")

        elif StatChosen == 2:
            CMGdata = datajson ['data'][0]['goals']
            CMAdata = datajson ['data'][0]['assists']
            CMPdata = datajson ['data'][0]['points']
            CMPPGdata = datajson ['data'][0]['pointsPerGame']
            print ("\n Connor McDavid had " + str(CMGdata) + " Goals, " + str(CMAdata) + " Assists, " + str(CMPdata) + " Points and " + str(CMPPGdata)+ " Points Per Game in 2017-2018. \n")

        elif StatChosen == 3:
            CMGWGdata = datajson ['data'][0]['gameWinningGoals']
            print ("\n Connor McDavid had " + str(CMGWGdata) + " Game Winning Goals in 2017-2018. \n")

        elif StatChosen == 4:
            CMPlusMdata = datajson ['data'][0]['plusMinus']
            print ("\n Connor McDavid had a " + str(CMPlusMdata) + " Plus/Minus in 2017-2018. \n")        
        
        elif StatChosen == 5:
            CMPMdata = datajson ['data'][0]['penaltyMinutes']
            print ("\n Connor McDavid had a " + str(CMPMdata) + " Penalty Minutes in 2017-2018. \n") 

        elif StatChosen == 6:
            CMPowerPGdata = datajson ['data'][0]['ppGoals']
            CMPPPdata = datajson ['data'][0]['ppPoints']
            print ("\n Connor McDavid had " + str(CMPowerPGdata) + " Power Play Goals and " + str(CMPPPdata) + " Power Play Points in 2017-2018. \n")     

        elif StatChosen == 7:
            CMSGdata = datajson ['data'][0]['shGoals']
            CMSPdata = datajson ['data'][0]['shPoints']
            print ("\n Connor McDavid had " + str(CMSGdata) + " Shorthanded Goals and " + str(CMSPdata) + " Shorthanded Points in 2017-2018. \n")

        elif StatChosen == 8:
            CMFcePcgdata = datajson ['data'][0]['faceoffWinPctg']
            CMSdata = datajson ['data'][0]['shots']
            CMShtPcgdata = datajson ['data'][0]['shootingPctg']
            print ("\n Connor McDavid had a " + str(CMFcePcgdata) + " Faceoff Percentage, " + str(CMSdata) + " Shots and a " + str(CMShtPcgdata) + " Shooting Percentage in 2017-2018. \n")

        elif StatChosen == 9:
            CMSPGdata = datajson ['data'][0]['shiftsPerGame']
            CMTIPGdata = datajson ['data'][0]['timeOnIcePerGame']
            print ("\n Connor McDavid had " + str(CMSPGdata) + " Shifts Per Game and " + str(CMTIPGdata) + " seconds on the ice per game in 2017-2018. \n")

        elif StatChosen == 10:
            CMBDdata = datajson ['data'][0]['playerBirthDate']
            CMBCitydata = datajson ['data'][0]['playerBirthCity']
            CMBPdata = datajson ['data'][0]['playerBirthStateProvince']
            CMBCdata = datajson ['data'][0]['playerBirthCountry']
            CMNdata = datajson ['data'][0]['playerNationality']
            print ("\n Connor McDavid was born on " + str(CMBDdata) + " in the city of " + str(CMBCitydata) + ", " + str(CMBPdata) + ", " + str(CMBCdata) + ". His nationality is " + str(CMNdata) + ". \n")

        elif StatChosen == 11:
            CMDOPNdata = datajson ['data'][0]['playerDraftOverallPickNo']
            CMRNdata = datajson ['data'][0]['playerDraftRoundNo']
            CMDYdata = datajson ['data'][0]['playerDraftYear']
            print ("\n Connor McDavid was drafted #" + str(CMDOPNdata) + " overall, in the #" + str(CMRNdata) + " round, in year " + str(CMDYdata) + ". \n") 

        elif StatChosen == 12:
            CMHdata = datajson ['data'][0]['playerHeight']
            CMWdata = datajson ['data'][0]['playerWeight']
            print ("\n Connor McDavid is " + str(CMHdata) + " inches tall and weighs " + str(CMWdata) + " pounds. \n")

        elif StatChosen == 13:
            CMPosdata = datajson ['data'][0]['playerPositionCode']
            CMSdata = datajson ['data'][0]['playerShootsCatches']
            CMTdata = datajson ['data'][0]['playerTeamsPlayedFor']
            print ("\n Connor McDavid plays " + str(CMPosdata) + "enter, Shoots " + str(CMSdata) + "eft, and played for " + str(CMTdata) + " in 2017-2018. \n")

        else:
            print("ERROR PLEASE TRY AGAIN")

















main()