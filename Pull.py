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

print (" Enter 1 for Connor McDavid. \n")
print (" Enter 2 for Claude Giroux. \n")
print (" Enter 3 for Nikita Kucherov. \n")
print (" Enter 4 for Evgeni Malkin. \n")
print (" Enter 5 for Nathan MacKinnon. \n")
print (" Enter 6 for Taylor Hall. \n")
print (" Enter 7 for Anze Kopitar. \n")
print (" Enter 8 for Phil Kessel. \n")
print (" Enter 9 for Blake Wheeler. \n")
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

    if ItemChosen == "1":

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

        StatChosen = int(input("Please make your selection. \n"))

    if StatChosen == "1":
        CMGPdata = datajson ['data'][0]['gamesPlayed']
        print ("\n Connor McDavid had " + str(CMGPdata) + " Games Played in 2017-2018. \n")

    elif StatChosen == "2":
        CMGdata = datajson ['data'][0]['goals']
        CMAdata = datajson ['data'][0]['assists']
        CMPdata = datajson ['data'][0]['points']
        CMPPGdata = datajson ['data'][0]['pointsPerGame']
        print ("\n Connor McDavid had " + str(CMGdata) + " Goals, " + str(CMAdata) + " Assists, " + str(CMPdata) + " Points and " + str(CMPPGdata)+ " Points Per Game in 2017-2018. \n")

    elif StatChosen == "3":
        CMGWGdata = datajson ['data'][0]['gameWinningGoals']
        print ("\n Connor McDavid had " + str(CMGWGdata) + " Game Winning Goals in 2017-2018. \n")

    elif StatChosen == "4":
        CMPlusMdata = datajson ['data'][0]['plusMinus']
        print ("\n Connor McDavid had a " + str(CMPlusMdata) + " Plus/Minus in 2017-2018. \n")        
    
    elif StatChosen == "5":
        CMPMdata = datajson ['data'][0]['penaltyMinutes']
        print ("\n Connor McDavid had a " + str(CMPMdata) + " Penalty Minutes in 2017-2018. \n") 

    elif StatChosen == "6":
        CMPowerPGdata = datajson ['data'][0]['ppGoals']
        CMPPPdata = datajson ['data'][0]['ppPoints']
        print ("\n Connor McDavid had " + str(CMPowerPGdata) + " Power Play Goals and " + str(CMPPPdata) + " Power Play Points in 2017-2018. \n")     

    elif StatChosen == "7":
        CMSGdata = datajson ['data'][0]['shGoals']
        CMSPdata = datajson ['data'][0]['shPoints']
        print ("\n Connor McDavid had " + str(CMSGdata) + " Shorthanded Goals and " + str(CMSPdata) + " Shorthanded Points in 2017-2018. \n")

    elif StatChosen == "8":
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

                                    #*********************** GIROUX ***********************

    if ItemChosen == "2":

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

        print (" Enter 13 for Position, Shoots/Catches, Team. HI \n")

        StatChosen = int(input("Please make your selection. \n"))

    if StatChosen == "1":
        CGGPdata = datajson ['data'][1]['gamesPlayed']
        print ("\n Claude Giroux had " + str(CGGPdata) + " Games Played in 2017-2018. \n")

    elif StatChosen == 2:
        Gdata = datajson ['data'][0]['goals']
        Adata = datajson ['data'][0]['assists']
        Pdata = datajson ['data'][0]['points']
        PPGdata = datajson ['data'][0]['pointsPerGame']
        print ("\n Connor McDavid had " + str(Gdata) + " Goals, " + str(Adata) + " Assists, " + str(Pdata) + " Points and " + str(PPGdata)+ " Points Per Game in 2017-2018. \n")

    elif StatChosen == 3:
        GWGdata = datajson ['data'][0]['gameWinningGoals']
        print ("\n Connor McDavid had " + str(GWGdata) + " Game Winning Goals in 2017-2018. \n")

    elif StatChosen == 4:
        PlusMdata = datajson ['data'][0]['plusMinus']
        print ("\n Connor McDavid had a " + str(PlusMdata) + " Plus/Minus in 2017-2018. \n")        
    
    elif StatChosen == 5:
        PMdata = datajson ['data'][0]['penaltyMinutes']
        print ("\n Connor McDavid had a " + str(PMdata) + " Penalty Minutes in 2017-2018. \n") 

    elif StatChosen == 6:
        PowerPGdata = datajson ['data'][0]['ppGoals']
        PPPdata = datajson ['data'][0]['ppPoints']
        print ("\n Connor McDavid had " + str(PowerPGdata) + " Power Play Goals and " + str(PPPdata) + " Power Play Points in 2017-2018. \n")     

    elif StatChosen == 7:
        SGdata = datajson ['data'][0]['shGoals']
        SPdata = datajson ['data'][0]['shPoints']
        print ("\n Connor McDavid had " + str(SGdata) + " Shorthanded Goals and " + str(SPdata) + " Shorthanded Points in 2017-2018. \n")

    elif StatChosen == 8:
        FcePcgdata = datajson ['data'][0]['faceoffWinPctg']
        Sdata = datajson ['data'][0]['shots']
        ShtPcgdata = datajson ['data'][0]['shootingPctg']
        print ("\n Connor McDavid had a " + str(FcePcgdata) + " Faceoff Percentage, " + str(Sdata) + " Shots and a " + str(ShtPcgdata) + " Shooting Percentage in 2017-2018. \n")

    elif StatChosen == 9:
        SPGdata = datajson ['data'][0]['shiftsPerGame']
        TIPGdata = datajson ['data'][0]['timeOnIcePerGame']
        print ("\n Connor McDavid had " + str(SPGdata) + " Shifts Per Game and " + str(TIPGdata) + " seconds on the ice per game in 2017-2018. \n")

    elif StatChosen == 10:
        BDdata = datajson ['data'][0]['playerBirthDate']
        BCitydata = datajson ['data'][0]['playerBirthCity']
        BPdata = datajson ['data'][0]['playerBirthStateProvince']
        BCdata = datajson ['data'][0]['playerBirthCountry']
        Ndata = datajson ['data'][0]['playerNationality']
        print ("\n Connor McDavid was born on " + str(BDdata) + " in the city of " + str(BCitydata) + ", " + str(BPdata) + ", " + str(BCdata) + ". His nationality is " + str(Ndata) + ". \n")

    elif StatChosen == 11:
        DOPNdata = datajson ['data'][0]['playerDraftOverallPickNo']
        RNdata = datajson ['data'][0]['playerDraftRoundNo']
        DYdata = datajson ['data'][0]['playerDraftYear']
        print ("\n Connor McDavid was drafted #" + str(DOPNdata) + " overall, in the #" + str(RNdata) + " round, in year " + str(DYdata) + ". \n") 

    elif StatChosen == 12:
        Hdata = datajson ['data'][0]['playerHeight']
        Wdata = datajson ['data'][0]['playerWeight']
        print ("\n Connor McDavid is " + str(Hdata) + " inches tall and weighs " + str(Wdata) + " pounds. \n")

    elif StatChosen == 13:
        Posdata = datajson ['data'][0]['playerPositionCode']
        Sdata = datajson ['data'][0]['playerShootsCatches']
        Tdata = datajson ['data'][0]['playerTeamsPlayedFor']
        print ("\n Connor McDavid plays " + str(Posdata) + "enter, Shoots " + str(Sdata) + "eft, and played for " + str(Tdata) + " in 2017-2018. \n")


main()
