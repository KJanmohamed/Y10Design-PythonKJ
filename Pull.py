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
print (" Enter 2 for Mitch Marner. \n")
print (" Enter 3 for Sidney Crosby. \n")
print (" Enter 4 for Auston Matthews. \n")
print (" Enter 5 for Nathan MacKinnon. \n")
ItemChosen = int(input("Please make your selection - if not a valid answer the program will not continue. \n"))

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









                                    #*********************** MARNER ***********************

    elif ItemChosen == 2:

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

        if StatChosen == 1:
            MMGPdata = datajson ['data'][38]['gamesPlayed']
            print ("\n Mitch Marner had " + str(MMGPdata) + " Games Played in 2017-2018. \n")

        elif StatChosen == 2:
            MMGdata = datajson ['data'][38]['goals']
            MMAdata = datajson ['data'][38]['assists']
            MMPdata = datajson ['data'][38]['points']
            MMPPGdata = datajson ['data'][38]['pointsPerGame']
            print ("\n Mitch Marner had " + str(MMGdata) + " Goals, " + str(MMAdata) + " Assists, " + str(MMPdata) + " Points and " + str(MMPPGdata)+ " Points Per Game in 2017-2018. \n")

        elif StatChosen == 3:
            MMGWGdata = datajson ['data'][38]['gameWinningGoals']
            print ("\n Mitch Marner had " + str(MMGWGdata) + " Game Winning Goals in 2017-2018. \n")

        elif StatChosen == 4:
            MMPlusMdata = datajson ['data'][38]['plusMinus']
            print ("\n Mitch Marner had a " + str(MMPlusMdata) + " Plus/Minus in 2017-2018. \n")        
        
        elif StatChosen == 5:
            MMPMdata = datajson ['data'][38]['penaltyMinutes']
            print ("\n Mitch Marner had a " + str(MMPMdata) + " Penalty Minutes in 2017-2018. \n") 

        elif StatChosen == 6:
            MMPowerPGdata = datajson ['data'][38]['ppGoals']
            MMPPPdata = datajson ['data'][0]['ppPoints']
            print ("\n Mitch Marner had " + str(MMPowerPGdata) + " Power Play Goals and " + str(MMPPPdata) + " Power Play Points in 2017-2018. \n")     

        elif StatChosen == 7:
            MMSGdata = datajson ['data'][38]['shGoals']
            MMSPdata = datajson ['data'][38]['shPoints']
            print ("\n Mitch Marner had " + str(MMSGdata) + " Shorthanded Goals and " + str(MMSPdata) + " Shorthanded Points in 2017-2018. \n")

        elif StatChosen == 8:
            MMFcePcgdata = datajson ['data'][38]['faceoffWinPctg']
            MMSdata = datajson ['data'][38]['shots']
            MMShtPcgdata = datajson ['data'][38]['shootingPctg']
            print ("\n Mitch Marner had a " + str(MMFcePcgdata) + " Faceoff Percentage, " + str(MMSdata) + " Shots and a " + str(MMShtPcgdata) + " Shooting Percentage in 2017-2018. \n")

        elif StatChosen == 9:
            MMSPGdata = datajson ['data'][38]['shiftsPerGame']
            MMTIPGdata = datajson ['data'][38]['timeOnIcePerGame']
            print ("\n Mitch Marner had " + str(MMSPGdata) + " Shifts Per Game and " + str(MMTIPGdata) + " seconds on the ice per game in 2017-2018. \n")

        elif StatChosen == 10:
            MMBDdata = datajson ['data'][38]['playerBirthDate']
            MMBCitydata = datajson ['data'][38]['playerBirthCity']
            MMBPdata = datajson ['data'][38]['playerBirthStateProvince']
            MMBCdata = datajson ['data'][38]['playerBirthCountry']
            MMNdata = datajson ['data'][38]['playerNationality']
            print ("\n Mitch Marner was born on " + str(MMBDdata) + " in the city of " + str(MMBCitydata) + ", " + str(MMBPdata) + ", " + str(MMBCdata) + ". His nationality is " + str(MMNdata) + ". \n")

        elif StatChosen == 11:
            MMDOPNdata = datajson ['data'][38]['playerDraftOverallPickNo']
            MMRNdata = datajson ['data'][38]['playerDraftRoundNo']
            MMDYdata = datajson ['data'][38]['playerDraftYear']
            print ("\n Mitch Marner was drafted #" + str(MMDOPNdata) + " overall, in the #" + str(MMRNdata) + " round, in year " + str(MMDYdata) + ". \n") 

        elif StatChosen == 12:
            MMHdata = datajson ['data'][38]['playerHeight']
            MMWdata = datajson ['data'][38]['playerWeight']
            print ("\n Mitch Marner is " + str(MMHdata) + " inches tall and weighs " + str(MMWdata) + " pounds. \n")

        elif StatChosen == 13:
            MMPosdata = datajson ['data'][38]['playerPositionCode']
            MMSdata = datajson ['data'][38]['playerShootsCatches']
            MMTdata = datajson ['data'][38]['playerTeamsPlayedFor']
            print ("\n Mitch Marner plays " + str(MMPosdata) + "enter, Shoots " + str(MMSdata) + "ight, and played for " + str(MMTdata) + " in 2017-2018. \n")





                                    #*********************** CROSBY ***********************

    elif ItemChosen == 3:

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

        if StatChosen == 1:
            SCGPdata = datajson ['data'][9]['gamesPlayed']
            print ("\n Sidney Crosby had " + str(SCGPdata) + " Games Played in 2017-2018. \n")

        elif StatChosen == 2:
            SCGdata = datajson ['data'][9]['goals']
            SCAdata = datajson ['data'][9]['assists']
            SCPdata = datajson ['data'][9]['points']
            SCPPGdata = datajson ['data'][9]['pointsPerGame']
            print ("\n Sidney Crosby had " + str(SCGdata) + " Goals, " + str(SCAdata) + " Assists, " + str(SCPdata) + " Points and " + str(SCPPGdata)+ " Points Per Game in 2017-2018. \n")

        elif StatChosen == 3:
            SCGWGdata = datajson ['data'][9]['gameWinningGoals']
            print ("\n Sidney Crosby had " + str(SCGWGdata) + " Game Winning Goals in 2017-2018. \n")

        elif StatChosen == 4:
            SCPlusMdata = datajson ['data'][9]['plusMinus']
            print ("\n Sidney Crosby had a " + str(SCPlusMdata) + " Plus/Minus in 2017-2018. \n")        
        
        elif StatChosen == 5:
            SCPMdata = datajson ['data'][9]['penaltyMinutes']
            print ("\n Sidney Crosby had a " + str(SCPMdata) + " Penalty Minutes in 2017-2018. \n") 

        elif StatChosen == 6:
            SCPowerPGdata = datajson ['data'][9]['ppGoals']
            SCPPPdata = datajson ['data'][9]['ppPoints']
            print ("\n Sidney Crosby had " + str(SCPowerPGdata) + " Power Play Goals and " + str(SCPPPdata) + " Power Play Points in 2017-2018. \n")     

        elif StatChosen == 7:
            SCSGdata = datajson ['data'][9]['shGoals']
            SCSPdata = datajson ['data'][9]['shPoints']
            print ("\n Sidney Crosby had " + str(SCSGdata) + " Shorthanded Goals and " + str(SCSPdata) + " Shorthanded Points in 2017-2018. \n")

        elif StatChosen == 8:
            SCFcePcgdata = datajson ['data'][9]['faceoffWinPctg']
            SCSdata = datajson ['data'][9]['shots']
            SCShtPcgdata = datajson ['data'][9]['shootingPctg']
            print ("\n Sidney Crosby had a " + str(SCFcePcgdata) + " Faceoff Percentage, " + str(SCSdata) + " Shots and a " + str(SCShtPcgdata) + " Shooting Percentage in 2017-2018. \n")

        elif StatChosen == 9:
            SCSPGdata = datajson ['data'][9]['shiftsPerGame']
            SCTIPGdata = datajson ['data'][9]['timeOnIcePerGame']
            print ("\n Sidney Crosby had " + str(SCSPGdata) + " Shifts Per Game and " + str(SCTIPGdata) + " seconds on the ice per game in 2017-2018. \n")

        elif StatChosen == 10:
            SCBDdata = datajson ['data'][9]['playerBirthDate']
            SCBCitydata = datajson ['data'][9]['playerBirthCity']
            SCBPdata = datajson ['data'][9]['playerBirthStateProvince']
            SCBCdata = datajson ['data'][9]['playerBirthCountry']
            SCNdata = datajson ['data'][9]['playerNationality']
            print ("\n Sidney Crosby was born on " + str(SCBDdata) + " in the city of " + str(SCBCitydata) + ", " + str(SCBPdata) + ", " + str(SCBCdata) + ". His nationality is " + str(SCNdata) + ". \n")

        elif StatChosen == 11:
            SCDOPNdata = datajson ['data'][9]['playerDraftOverallPickNo']
            SCRNdata = datajson ['data'][9]['playerDraftRoundNo']
            SCDYdata = datajson ['data'][9]['playerDraftYear']
            print ("\n Sidney Crosby was drafted #" + str(SCDOPNdata) + " overall, in the #" + str(SCRNdata) + " round, in year " + str(SCDYdata) + ". \n") 

        elif StatChosen == 12:
            SCHdata = datajson ['data'][9]['playerHeight']
            SCWdata = datajson ['data'][9]['playerWeight']
            print ("\n Sidney Crosby is " + str(SCHdata) + " inches tall and weighs " + str(SCWdata) + " pounds. \n")

        elif StatChosen == 13:
            SCPosdata = datajson ['data'][9]['playerPositionCode']
            SCSdata = datajson ['data'][9]['playerShootsCatches']
            SCTdata = datajson ['data'][9]['playerTeamsPlayedFor']
            print ("\n Sidney Crosby plays " + str(SCPosdata) + "enter, Shoots " + str(SCSdata) + "eft, and played for " + str(SCTdata) + " in 2017-2018. \n")

            
                                    #*********************** MATTHEWS ***********************

    elif ItemChosen == 4:

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

        if StatChosen == 1:
            AMGPdata = datajson ['data'][57]['gamesPlayed']
            print ("\n Auston Matthews had " + str(AMGPdata) + " Games Played in 2017-2018. \n")

        elif StatChosen == 2:
            AMGdata = datajson ['data'][57]['goals']
            AMAdata = datajson ['data'][57]['assists']
            AMPdata = datajson ['data'][57]['points']
            AMPPGdata = datajson ['data'][57]['pointsPerGame']
            print ("\n Auston Matthews had " + str(AMGdata) + " Goals, " + str(AMAdata) + " Assists, " + str(AMPdata) + " Points and " + str(AMPPGdata)+ " Points Per Game in 2017-2018. \n")

        elif StatChosen == 3:
            AMGWGdata = datajson ['data'][57]['gameWinningGoals']
            print ("\n Auston Matthews had " + str(AMGWGdata) + " Game Winning Goals in 2017-2018. \n")

        elif StatChosen == 4:
            AMPlusMdata = datajson ['data'][57]['plusMinus']
            print ("\n Auston Matthews had a " + str(AMPlusMdata) + " Plus/Minus in 2017-2018. \n")        
        
        elif StatChosen == 5:
            AMPMdata = datajson ['data'][57]['penaltyMinutes']
            print ("\n Auston Matthews had a " + str(AMPMdata) + " Penalty Minutes in 2017-2018. \n") 

        elif StatChosen == 6:
            AMPowerPGdata = datajson ['data'][57]['ppGoals']
            AMPPPdata = datajson ['data'][57]['ppPoints']
            print ("\n Auston Matthews had " + str(AMPowerPGdata) + " Power Play Goals and " + str(AMPPPdata) + " Power Play Points in 2017-2018. \n")     

        elif StatChosen == 7:
            AMSGdata = datajson ['data'][57]['shGoals']
            AMSPdata = datajson ['data'][57]['shPoints']
            print ("\n Auston Matthews had " + str(AMSGdata) + " Shorthanded Goals and " + str(AMSPdata) + " Shorthanded Points in 2017-2018. \n")

        elif StatChosen == 8:
            AMFcePcgdata = datajson ['data'][57]['faceoffWinPctg']
            AMSdata = datajson ['data'][57]['shots']
            AMShtPcgdata = datajson ['data'][57]['shootingPctg']
            print ("\n Auston Matthews had a " + str(AMFcePcgdata) + " Faceoff Percentage, " + str(AMSdata) + " Shots and a " + str(AMShtPcgdata) + " Shooting Percentage in 2017-2018. \n")

        elif StatChosen == 9:
            AMSPGdata = datajson ['data'][57]['shiftsPerGame']
            AMTIPGdata = datajson ['data'][57]['timeOnIcePerGame']
            print ("\n Auston Matthews had " + str(AMSPGdata) + " Shifts Per Game and " + str(AMTIPGdata) + " seconds on the ice per game in 2017-2018. \n")

        elif StatChosen == 10:
            AMBDdata = datajson ['data'][57]['playerBirthDate']
            AMBCitydata = datajson ['data'][57]['playerBirthCity']
            AMBPdata = datajson ['data'][57]['playerBirthStateProvince']
            AMBCdata = datajson ['data'][57]['playerBirthCountry']
            AMNdata = datajson ['data'][57]['playerNationality']
            print ("\n Auston Matthews was born on " + str(AMBDdata) + " in the city of " + str(AMBCitydata) + ", " + str(AMBPdata) + ", " + str(AMBCdata) + ". His nationality is " + str(AMNdata) + ". \n")

        elif StatChosen == 11:
            AMDOPNdata = datajson ['data'][57]['playerDraftOverallPickNo']
            AMRNdata = datajson ['data'][57]['playerDraftRoundNo']
            AMDYdata = datajson ['data'][57]['playerDraftYear']
            print ("\n Auston Matthews was drafted #" + str(AMDOPNdata) + " overall, in the #" + str(AMRNdata) + " round, in year " + str(AMDYdata) + ". \n") 

        elif StatChosen == 12:
            AMHdata = datajson ['data'][57]['playerHeight']
            AMWdata = datajson ['data'][57]['playerWeight']
            print ("\n Auston Matthews is " + str(AMHdata) + " inches tall and weighs " + str(AMWdata) + " pounds. \n")

        elif StatChosen == 13:
            AMPosdata = datajson ['data'][57]['playerPositionCode']
            AMSdata = datajson ['data'][57]['playerShootsCatches']
            AMTdata = datajson ['data'][57]['playerTeamsPlayedFor']
            print ("\n Auston Matthews plays " + str(AMPosdata) + "enter, Shoots " + str(AMSdata) + "eft, and played for " + str(AMTdata) + " in 2017-2018. \n")

                                                                       #*********************** MACKINNON ***********************

    elif ItemChosen == 5:

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

        if StatChosen == 1:
            NMGPdata = datajson ['data'][4]['gamesPlayed']
            print ("\n Nathan MacKinnon had " + str(NMGPdata) + " Games Played in 2017-2018. \n")

        elif StatChosen == 2:
            NMGdata = datajson ['data'][4]['goals']
            NMAdata = datajson ['data'][4]['assists']
            NMPdata = datajson ['data'][4]['points']
            NMPPGdata = datajson ['data'][4]['pointsPerGame']
            print ("\n Nathan MacKinnon had " + str(NMGdata) + " Goals, " + str(NMAdata) + " Assists, " + str(NMPdata) + " Points and " + str(NMPPGdata)+ " Points Per Game in 2017-2018. \n")

        elif StatChosen == 3:
            NMGWGdata = datajson ['data'][4]['gameWinningGoals']
            print ("\n Nathan MacKinnon had " + str(NMGWGdata) + " Game Winning Goals in 2017-2018. \n")

        elif StatChosen == 4:
            NMPlusMdata = datajson ['data'][4]['plusMinus']
            print ("\n Nathan MacKinnon had a " + str(NMPlusMdata) + " Plus/Minus in 2017-2018. \n")        
        
        elif StatChosen == 5:
            NMPMdata = datajson ['data'][4]['penaltyMinutes']
            print ("\n Nathan MacKinnon had a " + str(NMPMdata) + " Penalty Minutes in 2017-2018. \n") 

        elif StatChosen == 6:
            NMPowerPGdata = datajson ['data'][4]['ppGoals']
            NMPPPdata = datajson ['data'][4]['ppPoints']
            print ("\n Nathan MacKinnon had " + str(NMPowerPGdata) + " Power Play Goals and " + str(NMPPPdata) + " Power Play Points in 2017-2018. \n")     

        elif StatChosen == 7:
            NMSGdata = datajson ['data'][4]['shGoals']
            NMSPdata = datajson ['data'][4]['shPoints']
            print ("\n Nathan MacKinnon had " + str(NMSGdata) + " Shorthanded Goals and " + str(NMSPdata) + " Shorthanded Points in 2017-2018. \n")

        elif StatChosen == 8:
            NMFcePcgdata = datajson ['data'][4]['faceoffWinPctg']
            NMSdata = datajson ['data'][4]['shots']
            NMShtPcgdata = datajson ['data'][4]['shootingPctg']
            print ("\n Nathan MacKinnon had a " + str(NMFcePcgdata) + " Faceoff Percentage, " + str(NMSdata) + " Shots and a " + str(NMShtPcgdata) + " Shooting Percentage in 2017-2018. \n")

        elif StatChosen == 9:
            NMSPGdata = datajson ['data'][4]['shiftsPerGame']
            NMTIPGdata = datajson ['data'][4]['timeOnIcePerGame']
            print ("\n Nathan MacKinnon had " + str(NMSPGdata) + " Shifts Per Game and " + str(NMTIPGdata) + " seconds on the ice per game in 2017-2018. \n")

        elif StatChosen == 10:
            NMBDdata = datajson ['data'][4]['playerBirthDate']
            NMBCitydata = datajson ['data'][4]['playerBirthCity']
            NMBPdata = datajson ['data'][4]['playerBirthStateProvince']
            NMBCdata = datajson ['data'][4]['playerBirthCountry']
            NMNdata = datajson ['data'][4]['playerNationality']
            print ("\n Nathan MacKinnon was born on " + str(NMBDdata) + " in the city of " + str(NMBCitydata) + ", " + str(NMBPdata) + ", " + str(NMBCdata) + ". His nationality is " + str(NMNdata) + ". \n")

        elif StatChosen == 11:
            NMDOPNdata = datajson ['data'][4]['playerDraftOverallPickNo']
            NMRNdata = datajson ['data'][4]['playerDraftRoundNo']
            NMDYdata = datajson ['data'][4]['playerDraftYear']
            print ("\n Nathan MacKinnon was drafted #" + str(NMDOPNdata) + " overall, in the #" + str(NMRNdata) + " round, in year " + str(NMDYdata) + ". \n") 

        elif StatChosen == 12:
            NMHdata = datajson ['data'][4]['playerHeight']
            NMWdata = datajson ['data'][4]['playerWeight']
            print ("\n Nathan MacKinnon is " + str(NMHdata) + " inches tall and weighs " + str(NMWdata) + " pounds. \n")

        elif StatChosen == 13:
            NMPosdata = datajson ['data'][4]['playerPositionCode']
            NMSdata = datajson ['data'][4]['playerShootsCatches']
            NMTdata = datajson ['data'][4]['playerTeamsPlayedFor']
            print ("\n Nathan MacKinnon plays " + str(NMPosdata) + "enter, Shoots " + str(NMSdata) + "ight, and played for " + str(NMTdata) + " in 2017-2018. \n")


main()