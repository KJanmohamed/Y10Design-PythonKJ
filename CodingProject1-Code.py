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

def writeHTML(data):
    myfile = open("myapi.html","w") # use "a" to "append"    
    myfile.write("""
    <html>
<title></title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato">
<style>
body {font-family:'Lato';}
body {
  font-size: 15px;
}
#navbar {
  list-style-type: none;
  margin: 1;
  padding: 0;
  overflow: hidden;
  background-color: #2196F3;
  position: -webkit-sticky;
  position: sticky;
  top: 0;
}
#navbar li {
  float: left;
}
#navbar li a {
  display: block;
  color: black;
  text-align: center;
  padding: 18px 20px;
  text-decoration: none;
}
#navbar li a:hover {
  background-color: #fff;
}
.active {
  background-color: #2196F3;
}
.flex-container {
  display: flex;
  flex-wrap: nowrap;
  background-color: #fff;
  justify-content: center;
  padding: 25px 16px
}
.flex-container > div {
  background-color: #2196F3;
  height: 200px;
  width: 200px;
  margin: 10px;
  text-align: center;
  line-height: 75px;
  font-size: 30px;
  padding: 25px 16px
}
#header {
  text-align:center;
  font-size: 30px;
  color: #ffff;
  background-color: #2196F3;
  padding: 10px 16px
}
#text {
  text-align:center;
  padding: 25px 16px
}
#BulletList {
  background-color:none;
  text-align:center;
  padding-bottom: 10px
}
#Lines {
  line-height:40px;
}
</style>

<body>

<!-- NavBar -->

<ul id="navbar">
  <li><a class="active" href="https://sites.google.com/s/1feEjHtDfItZ9hj9SFVzhy2tqFrSo_1m7/p/1IaQe7paEabex_MX7L_sNV1dUlMimfGfh/edit"> MY GOOGLE SITE </a></li>

  <li><a href="https://sites.google.com/ucc.on.ca/year9designcoding-kjanmohamed/introduction-year-10"> ABOUT ME </a></li>

  <li style="float:right"><a href="https://github.com/KJanmohamed/Y10Design-PythonKJ/blob/master/CodingProject1-Code.py"> LINK TO THE CODE </a></li>

  <li style="float:right"><a href="https://github.com/KJanmohamed"> MY GITHUB </a></li>


</ul>

<p id="header"> 2017-2018 NHL STATS PAGE! </p>

<center>
  <image src="Images/2017_NHL_Winter_Classic_logo.png" style="width:300px; height:300px;"><image src="Images/220px-2018_NHL_Winter_Classic_logo.png" style="width:300px; height:300px;"></image>
</center>

<!-- PARAGRAPH -->

<p id="header"> The Data you requested is: </p>

<p id="text" > """+ data+""" </p>

<p id="header" > SHORT SUMMARY </p>

<p id="text" > </p> 

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
            writeHTML( "Connor McDavid had " + str(CMGPdata) + " Games Played in 2017-2018. \n")

        #                                           *-------------- GOALS, ASSISTS, POINTS, POINTS PER GAME -----------------*

        elif StatChosen == 2:

            CMGdata = datajson ['data'][0]['goals']
            CMAdata = datajson ['data'][0]['assists']
            CMPdata = datajson ['data'][0]['points']
            CMPPGdata = datajson ['data'][0]['pointsPerGame']
            writeHTML( "Connor McDavid had " + str(CMGdata) + " Goals, " + str(CMAdata) + " Assists, " + str(CMPdata) + " Points and " + str(CMPPGdata)+ " Points Per Game in 2017-2018. \n")
        #                                           *-------------- GAME WINNING GOALS -----------------*

        elif StatChosen == 3:

            CMGWGdata = datajson ['data'][0]['gameWinningGoals']
            writeHTML( "Connor McDavid had " + str(CMGWGdata) + " Game Winning Goals in 2017-2018. \n")

        #                                           *-------------- PLUS/MINUS -----------------*

        elif StatChosen == 4:

            CMPlusMdata = datajson ['data'][0]['plusMinus']
            writeHTML( "Connor McDavid had a " + str(CMPlusMdata) + " Plus/Minus in 2017-2018. \n")        

        #                                           *-------------- PENALTY MINUTES -----------------*

        elif StatChosen == 5:

            CMPMdata = datajson ['data'][0]['penaltyMinutes']
            writeHTML( "Connor McDavid had a " + str(CMPMdata) + " Penalty Minutes in 2017-2018. \n") 

        #                                           *-------------- POWER PLAY GOALS AND POINTS -----------------*

        elif StatChosen == 6:

            CMPowerPGdata = datajson ['data'][0]['ppGoals']
            CMPPPdata = datajson ['data'][0]['ppPoints']
            writeHTML( "Connor McDavid had " + str(CMPowerPGdata) + " Power Play Goals and " + str(CMPPPdata) + " Power Play Points in 2017-2018. \n")     

        #                                           *-------------- SHORTHANDED GOALS AND POINTS -----------------*

        elif StatChosen == 7:

            CMSGdata = datajson ['data'][0]['shGoals']
            CMSPdata = datajson ['data'][0]['shPoints']
            writeHTML( "Connor McDavid had " + str(CMSGdata) + " Shorthanded Goals and " + str(CMSPdata) + " Shorthanded Points in 2017-2018. \n")

        #                                           *-------------- FACEOFF PERCENTAGE/SHOTS/SHOOTING PERCENTGE -----------------*

        elif StatChosen == 8:

            CMFcePcgdata = datajson ['data'][0]['faceoffWinPctg']
            CMSdata = datajson ['data'][0]['shots']
            CMShtPcgdata = datajson ['data'][0]['shootingPctg']
            writeHTML( "Connor McDavid had a " + str(CMFcePcgdata) + " Faceoff Percentage, " + str(CMSdata) + " Shots and a " + str(CMShtPcgdata) + " Shooting Percentage in 2017-2018. \n")

        #                                           *-------------- SHIFTS PER GAME AND ICE TIME -----------------*

        elif StatChosen == 9:

            CMSPGdata = datajson ['data'][0]['shiftsPerGame']
            CMTIPGdata = datajson ['data'][0]['timeOnIcePerGame']
            writeHTML( "Connor McDavid had " + str(CMSPGdata) + " Shifts Per Game and " + str(CMTIPGdata) + " seconds on the ice per game in 2017-2018. \n")

        #                                           *-------------- PERSONAL INFO -----------------*

        elif StatChosen == 10:

            CMBDdata = datajson ['data'][0]['playerBirthDate']
            CMBCitydata = datajson ['data'][0]['playerBirthCity']
            CMBPdata = datajson ['data'][0]['playerBirthStateProvince']
            CMBCdata = datajson ['data'][0]['playerBirthCountry']
            CMNdata = datajson ['data'][0]['playerNationality']
            writeHTML( "Connor McDavid was born on " + str(CMBDdata) + " in the city of " + str(CMBCitydata) + ", " + str(CMBPdata) + ", " + str(CMBCdata) + ". His nationality is " + str(CMNdata) + ". \n")

        #                                           *-------------- DRAFT PICK INFO -----------------*

        elif StatChosen == 11:

            CMDOPNdata = datajson ['data'][0]['playerDraftOverallPickNo']
            CMRNdata = datajson ['data'][0]['playerDraftRoundNo']
            CMDYdata = datajson ['data'][0]['playerDraftYear']
            writeHTML( "Connor McDavid was drafted #" + str(CMDOPNdata) + " overall, in the #" + str(CMRNdata) + " round, in year " + str(CMDYdata) + ". \n") 

        #                                           *-------------- HEIGHT AND WEIGHT -----------------*

        elif StatChosen == 12:

            CMHdata = datajson ['data'][0]['playerHeight']
            CMWdata = datajson ['data'][0]['playerWeight']
            writeHTML( "Connor McDavid is " + str(CMHdata) + " inches tall and weighs " + str(CMWdata) + " pounds. \n")

        #                                           *-------------- POSITION/SHOOTS/TEAM -----------------*

        elif StatChosen == 13:

            CMPosdata = datajson ['data'][0]['playerPositionCode']
            CMSdata = datajson ['data'][0]['playerShootsCatches']
            CMTdata = datajson ['data'][0]['playerTeamsPlayedFor']
            writeHTML( "Connor McDavid plays " + str(CMPosdata) + "enter, Shoots " + str(CMSdata) + "eft, and played for " + str(CMTdata) + " in 2017-2018. \n")

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

        #                                           *--------------  STAT CHOSEN VARIABLE -----------------*

        StatChosen = int(input("Please make your selection. \n"))

        #                                           *--------------  GAMES PLAYED -----------------*

        if StatChosen == 1:

            MMGPdata = datajson ['data'][38]['gamesPlayed']
            writeHTML( "Mitch Marner had " + str(MMGPdata) + " Games Played in 2017-2018. \n")


        #                                           *-------------- GOALS, ASSISTS, POINTS, POINTS PER GAME -----------------*

        elif StatChosen == 2:

            MMGdata = datajson ['data'][38]['goals']
            MMAdata = datajson ['data'][38]['assists']
            MMPdata = datajson ['data'][38]['points']
            MMPPGdata = datajson ['data'][38]['pointsPerGame']
            writeHTML( "Mitch Marner had " + str(MMGdata) + " Goals, " + str(MMAdata) + " Assists, " + str(MMPdata) + " Points and " + str(MMPPGdata)+ " Points Per Game in 2017-2018. \n")

        #                                           *-------------- GAME WINNING GOALS -----------------*

        elif StatChosen == 3:

            MMGWGdata = datajson ['data'][38]['gameWinningGoals']
            writeHTML( "Mitch Marner had " + str(MMGWGdata) + " Game Winning Goals in 2017-2018. \n")

        #                                           *-------------- PLUS/MINUS -----------------*

        elif StatChosen == 4:

            MMPlusMdata = datajson ['data'][38]['plusMinus']
            writeHTML( "Mitch Marner had a " + str(MMPlusMdata) + " Plus/Minus in 2017-2018. \n")        

        #                                           *-------------- PENALTY MINUTES -----------------*

        elif StatChosen == 5:

            MMPMdata = datajson ['data'][38]['penaltyMinutes']
            writeHTML( "Mitch Marner had a " + str(MMPMdata) + " Penalty Minutes in 2017-2018. \n") 

        #                                           *-------------- POWER PLAY GOALS AND POINTS -----------------*

        elif StatChosen == 6:

            MMPowerPGdata = datajson ['data'][38]['ppGoals']
            MMPPPdata = datajson ['data'][0]['ppPoints']
            writeHTML( "Mitch Marner had " + str(MMPowerPGdata) + " Power Play Goals and " + str(MMPPPdata) + " Power Play Points in 2017-2018. \n")     

        #                                           *-------------- SHORTHANDED GOALS AND POINTS -----------------*

        elif StatChosen == 7:

            MMSGdata = datajson ['data'][38]['shGoals']
            MMSPdata = datajson ['data'][38]['shPoints']
            writeHTML( "Mitch Marner had " + str(MMSGdata) + " Shorthanded Goals and " + str(MMSPdata) + " Shorthanded Points in 2017-2018. \n")

        #                                           *-------------- FACEOFF PERCENTAGE/SHOTS/SHOOTING PERCENTGE -----------------*

        elif StatChosen == 8:

            MMFcePcgdata = datajson ['data'][38]['faceoffWinPctg']
            MMSdata = datajson ['data'][38]['shots']
            MMShtPcgdata = datajson ['data'][38]['shootingPctg']
            writeHTML( "Mitch Marner had a " + str(MMFcePcgdata) + " Faceoff Percentage, " + str(MMSdata) + " Shots and a " + str(MMShtPcgdata) + " Shooting Percentage in 2017-2018. \n")

        #                                           *-------------- SHIFTS PER GAME AND ICE TIME -----------------*

        elif StatChosen == 9:

            MMSPGdata = datajson ['data'][38]['shiftsPerGame']
            MMTIPGdata = datajson ['data'][38]['timeOnIcePerGame']
            writeHTML( "Mitch Marner had " + str(MMSPGdata) + " Shifts Per Game and " + str(MMTIPGdata) + " seconds on the ice per game in 2017-2018. \n")

        #                                           *-------------- PERSONAL INFO -----------------*

        elif StatChosen == 10:

            MMBDdata = datajson ['data'][38]['playerBirthDate']
            MMBCitydata = datajson ['data'][38]['playerBirthCity']
            MMBPdata = datajson ['data'][38]['playerBirthStateProvince']
            MMBCdata = datajson ['data'][38]['playerBirthCountry']
            MMNdata = datajson ['data'][38]['playerNationality']
            writeHTML( "Mitch Marner was born on " + str(MMBDdata) + " in the city of " + str(MMBCitydata) + ", " + str(MMBPdata) + ", " + str(MMBCdata) + ". His nationality is " + str(MMNdata) + ". \n")

        #                                           *-------------- DRAFT PICK INFO -----------------*

        elif StatChosen == 11:

            MMDOPNdata = datajson ['data'][38]['playerDraftOverallPickNo']
            MMRNdata = datajson ['data'][38]['playerDraftRoundNo']
            MMDYdata = datajson ['data'][38]['playerDraftYear']
            writeHTML( "Mitch Marner was drafted #" + str(MMDOPNdata) + " overall, in the #" + str(MMRNdata) + " round, in year " + str(MMDYdata) + ". \n") 

        #                                           *-------------- HEIGHT AND WEIGHT -----------------*

        elif StatChosen == 12:

            MMHdata = datajson ['data'][38]['playerHeight']
            MMWdata = datajson ['data'][38]['playerWeight']
            writeHTML( "Mitch Marner is " + str(MMHdata) + " inches tall and weighs " + str(MMWdata) + " pounds. \n")

        #                                           *-------------- POSITION/SHOOTS/TEAM -----------------*

        elif StatChosen == 13:

            MMPosdata = datajson ['data'][38]['playerPositionCode']
            MMSdata = datajson ['data'][38]['playerShootsCatches']
            MMTdata = datajson ['data'][38]['playerTeamsPlayedFor']
            writeHTML( "Mitch Marner plays " + str(MMPosdata) + "enter, Shoots " + str(MMSdata) + "ight, and played for " + str(MMTdata) + " in 2017-2018. \n")

        else:

            print("ERROR PLEASE TRY AGAIN")    



















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

        #                                           *--------------  STAT CHOSEN VARIABLE -----------------*

        StatChosen = int(input("Please make your selection. \n"))

        #                                           *--------------  GAMES PLAYED -----------------*

        if StatChosen == 1:

            SCGPdata = datajson ['data'][9]['gamesPlayed']
            writeHTML( "Sidney Crosby had " + str(SCGPdata) + " Games Played in 2017-2018. \n")

        #                                           *-------------- GOALS, ASSISTS, POINTS, POINTS PER GAME -----------------*

        elif StatChosen == 2:

            SCGdata = datajson ['data'][9]['goals']
            SCAdata = datajson ['data'][9]['assists']
            SCPdata = datajson ['data'][9]['points']
            SCPPGdata = datajson ['data'][9]['pointsPerGame']
            writeHTML( "Sidney Crosby had " + str(SCGdata) + " Goals, " + str(SCAdata) + " Assists, " + str(SCPdata) + " Points and " + str(SCPPGdata)+ " Points Per Game in 2017-2018. \n")

        #                                           *-------------- GAME WINNING GOALS -----------------*

        elif StatChosen == 3:

            SCGWGdata = datajson ['data'][9]['gameWinningGoals']
            writeHTML( "Sidney Crosby had " + str(SCGWGdata) + " Game Winning Goals in 2017-2018. \n")

        #                                           *-------------- PLUS/MINUS -----------------*

        elif StatChosen == 4:

            SCPlusMdata = datajson ['data'][9]['plusMinus']
            writeHTML( "Sidney Crosby had a " + str(SCPlusMdata) + " Plus/Minus in 2017-2018. \n")        
        
        #                                           *-------------- PENALTY MINUTES -----------------*

        elif StatChosen == 5:

            SCPMdata = datajson ['data'][9]['penaltyMinutes']
            writeHTML( "Sidney Crosby had a " + str(SCPMdata) + " Penalty Minutes in 2017-2018. \n") 

        #                                           *-------------- POWER PLAY GOALS AND POINTS -----------------*

        elif StatChosen == 6:

            SCPowerPGdata = datajson ['data'][9]['ppGoals']
            SCPPPdata = datajson ['data'][9]['ppPoints']
            writeHTML( "Sidney Crosby had " + str(SCPowerPGdata) + " Power Play Goals and " + str(SCPPPdata) + " Power Play Points in 2017-2018. \n")     

        #                                           *-------------- SHORTHANDED GOALS AND POINTS -----------------*

        elif StatChosen == 7:

            SCSGdata = datajson ['data'][9]['shGoals']
            SCSPdata = datajson ['data'][9]['shPoints']
            writeHTML( "Sidney Crosby had " + str(SCSGdata) + " Shorthanded Goals and " + str(SCSPdata) + " Shorthanded Points in 2017-2018. \n")

        #                                           *-------------- FACEOFF PERCENTAGE/SHOTS/SHOOTING PERCENTGE -----------------*

        elif StatChosen == 8:

            SCFcePcgdata = datajson ['data'][9]['faceoffWinPctg']
            SCSdata = datajson ['data'][9]['shots']
            SCShtPcgdata = datajson ['data'][9]['shootingPctg']
            writeHTML( "Sidney Crosby had a " + str(SCFcePcgdata) + " Faceoff Percentage, " + str(SCSdata) + " Shots and a " + str(SCShtPcgdata) + " Shooting Percentage in 2017-2018. \n")

        #                                           *-------------- SHIFTS PER GAME AND ICE TIME -----------------*

        elif StatChosen == 9:

            SCSPGdata = datajson ['data'][9]['shiftsPerGame']
            SCTIPGdata = datajson ['data'][9]['timeOnIcePerGame']
            writeHTML( "Sidney Crosby had " + str(SCSPGdata) + " Shifts Per Game and " + str(SCTIPGdata) + " seconds on the ice per game in 2017-2018. \n")

        #                                           *-------------- PERSONAL INFO -----------------*

        elif StatChosen == 10:

            SCBDdata = datajson ['data'][9]['playerBirthDate']
            SCBCitydata = datajson ['data'][9]['playerBirthCity']
            SCBPdata = datajson ['data'][9]['playerBirthStateProvince']
            SCBCdata = datajson ['data'][9]['playerBirthCountry']
            SCNdata = datajson ['data'][9]['playerNationality']
            writeHTML( "Sidney Crosby was born on " + str(SCBDdata) + " in the city of " + str(SCBCitydata) + ", " + str(SCBPdata) + ", " + str(SCBCdata) + ". His nationality is " + str(SCNdata) + ". \n")

        #                                           *-------------- DRAFT PICK INFO -----------------*

        elif StatChosen == 11:

            SCDOPNdata = datajson ['data'][9]['playerDraftOverallPickNo']
            SCRNdata = datajson ['data'][9]['playerDraftRoundNo']
            SCDYdata = datajson ['data'][9]['playerDraftYear']
            writeHTML( "Sidney Crosby was drafted #" + str(SCDOPNdata) + " overall, in the #" + str(SCRNdata) + " round, in year " + str(SCDYdata) + ". \n") 

        #                                           *-------------- HEIGHT AND WEIGHT -----------------*

        elif StatChosen == 12:

            SCHdata = datajson ['data'][9]['playerHeight']
            SCWdata = datajson ['data'][9]['playerWeight']
            writeHTML( "Sidney Crosby is " + str(SCHdata) + " inches tall and weighs " + str(SCWdata) + " pounds. \n")

        #                                           *-------------- POSITION/SHOOTS/TEAM -----------------*

        elif StatChosen == 13:

            SCPosdata = datajson ['data'][9]['playerPositionCode']
            SCSdata = datajson ['data'][9]['playerShootsCatches']
            SCTdata = datajson ['data'][9]['playerTeamsPlayedFor']
            writeHTML( "Sidney Crosby plays " + str(SCPosdata) + "enter, Shoots " + str(SCSdata) + "eft, and played for " + str(SCTdata) + " in 2017-2018. \n")

        else:
            print("ERROR PLEASE TRY AGAIN")















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

        #                                           *--------------  STAT CHOSEN VARIABLE -----------------*

        StatChosen = int(input("Please make your selection. \n"))

        #                                           *--------------  GAMES PLAYED -----------------*

        if StatChosen == 1:

            AMGPdata = datajson ['data'][57]['gamesPlayed']
            writeHTML( "Auston Matthews had " + str(AMGPdata) + " Games Played in 2017-2018. \n")

        #                                           *-------------- GOALS, ASSISTS, POINTS, POINTS PER GAME -----------------*

        elif StatChosen == 2:

            AMGdata = datajson ['data'][57]['goals']
            AMAdata = datajson ['data'][57]['assists']
            AMPdata = datajson ['data'][57]['points']
            AMPPGdata = datajson ['data'][57]['pointsPerGame']
            writeHTML( "Auston Matthews had " + str(AMGdata) + " Goals, " + str(AMAdata) + " Assists, " + str(AMPdata) + " Points and " + str(AMPPGdata)+ " Points Per Game in 2017-2018. \n")

        #                                           *-------------- GAME WINNING GOALS -----------------*

        elif StatChosen == 3:

            AMGWGdata = datajson ['data'][57]['gameWinningGoals']
            writeHTML( "Auston Matthews had " + str(AMGWGdata) + " Game Winning Goals in 2017-2018. \n")

        #                                           *-------------- PLUS/MINUS -----------------*

        elif StatChosen == 4:

            AMPlusMdata = datajson ['data'][57]['plusMinus']
            writeHTML( "Auston Matthews had a " + str(AMPlusMdata) + " Plus/Minus in 2017-2018. \n")        
        
        #                                           *-------------- PENALTY MINUTES -----------------*

        elif StatChosen == 5:

            AMPMdata = datajson ['data'][57]['penaltyMinutes']
            writeHTML( "Auston Matthews had a " + str(AMPMdata) + " Penalty Minutes in 2017-2018. \n") 

        #                                           *-------------- POWER PLAY GOALS AND POINTS -----------------*

        elif StatChosen == 6:

            AMPowerPGdata = datajson ['data'][57]['ppGoals']
            AMPPPdata = datajson ['data'][57]['ppPoints']
            writeHTML( "Auston Matthews had " + str(AMPowerPGdata) + " Power Play Goals and " + str(AMPPPdata) + " Power Play Points in 2017-2018. \n")     

        #                                           *-------------- SHORTHANDED GOALS AND POINTS -----------------*

        elif StatChosen == 7:

            AMSGdata = datajson ['data'][57]['shGoals']
            AMSPdata = datajson ['data'][57]['shPoints']
            writeHTML( "Auston Matthews had " + str(AMSGdata) + " Shorthanded Goals and " + str(AMSPdata) + " Shorthanded Points in 2017-2018. \n")

        #                                           *-------------- FACEOFF PERCENTAGE/SHOTS/SHOOTING PERCENTGE -----------------*

        elif StatChosen == 8:

            AMFcePcgdata = datajson ['data'][57]['faceoffWinPctg']
            AMSdata = datajson ['data'][57]['shots']
            AMShtPcgdata = datajson ['data'][57]['shootingPctg']
            writeHTML( "Auston Matthews had a " + str(AMFcePcgdata) + " Faceoff Percentage, " + str(AMSdata) + " Shots and a " + str(AMShtPcgdata) + " Shooting Percentage in 2017-2018. \n")

        #                                           *-------------- SHIFTS PER GAME AND ICE TIME -----------------*

        elif StatChosen == 9:

            AMSPGdata = datajson ['data'][57]['shiftsPerGame']
            AMTIPGdata = datajson ['data'][57]['timeOnIcePerGame']
            writeHTML( "Auston Matthews had " + str(AMSPGdata) + " Shifts Per Game and " + str(AMTIPGdata) + " seconds on the ice per game in 2017-2018. \n")

        #                                           *-------------- PERSONAL INFO -----------------*

        elif StatChosen == 10:

            AMBDdata = datajson ['data'][57]['playerBirthDate']
            AMBCitydata = datajson ['data'][57]['playerBirthCity']
            AMBPdata = datajson ['data'][57]['playerBirthStateProvince']
            AMBCdata = datajson ['data'][57]['playerBirthCountry']
            AMNdata = datajson ['data'][57]['playerNationality']
            writeHTML( "Auston Matthews was born on " + str(AMBDdata) + " in the city of " + str(AMBCitydata) + ", " + str(AMBPdata) + ", " + str(AMBCdata) + ". His nationality is " + str(AMNdata) + ". \n")

        #                                           *-------------- DRAFT PICK INFO -----------------*

        elif StatChosen == 11:

            AMDOPNdata = datajson ['data'][57]['playerDraftOverallPickNo']
            AMRNdata = datajson ['data'][57]['playerDraftRoundNo']
            AMDYdata = datajson ['data'][57]['playerDraftYear']
            writeHTML( "Auston Matthews was drafted #" + str(AMDOPNdata) + " overall, in the #" + str(AMRNdata) + " round, in year " + str(AMDYdata) + ". \n") 

        #                                           *-------------- HEIGHT AND WEIGHT -----------------*

        elif StatChosen == 12:

            AMHdata = datajson ['data'][57]['playerHeight']
            AMWdata = datajson ['data'][57]['playerWeight']
            writeHTML( "Auston Matthews is " + str(AMHdata) + " inches tall and weighs " + str(AMWdata) + " pounds. \n")

        #                                           *-------------- POSITION/SHOOTS/TEAM -----------------*

        elif StatChosen == 13:

            AMPosdata = datajson ['data'][57]['playerPositionCode']
            AMSdata = datajson ['data'][57]['playerShootsCatches']
            AMTdata = datajson ['data'][57]['playerTeamsPlayedFor']
            writeHTML( "Auston Matthews plays " + str(AMPosdata) + "enter, Shoots " + str(AMSdata) + "eft, and played for " + str(AMTdata) + " in 2017-2018. \n")

        else:
            print("ERROR PLEASE TRY AGAIN")

















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

        #                                           *--------------  STAT CHOSEN VARIABLE -----------------*

        StatChosen = int(input("Please make your selection. \n"))

        #                                           *--------------  GAMES PLAYED -----------------*

        if StatChosen == 1:

            NMGPdata = datajson ['data'][4]['gamesPlayed']
            writeHTML( "Nathan MacKinnon had " + str(NMGPdata) + " Games Played in 2017-2018. \n")

        #                                           *-------------- GOALS, ASSISTS, POINTS, POINTS PER GAME -----------------*

        elif StatChosen == 2:

            NMGdata = datajson ['data'][4]['goals']
            NMAdata = datajson ['data'][4]['assists']
            NMPdata = datajson ['data'][4]['points']
            NMPPGdata = datajson ['data'][4]['pointsPerGame']
            writeHTML( "Nathan MacKinnon had " + str(NMGdata) + " Goals, " + str(NMAdata) + " Assists, " + str(NMPdata) + " Points and " + str(NMPPGdata)+ " Points Per Game in 2017-2018. \n")

        #                                           *-------------- GAME WINNING GOALS -----------------*

        elif StatChosen == 3:

            NMGWGdata = datajson ['data'][4]['gameWinningGoals']
            writeHTML( "Nathan MacKinnon had " + str(NMGWGdata) + " Game Winning Goals in 2017-2018. \n")

        #                                           *-------------- PLUS/MINUS -----------------*

        elif StatChosen == 4:

            NMPlusMdata = datajson ['data'][4]['plusMinus']
            writeHTML( "Nathan MacKinnon had a " + str(NMPlusMdata) + " Plus/Minus in 2017-2018. \n")        
        
        #                                           *-------------- PENALTY MINUTES -----------------*

        elif StatChosen == 5:

            NMPMdata = datajson ['data'][4]['penaltyMinutes']
            writeHTML( "Nathan MacKinnon had a " + str(NMPMdata) + " Penalty Minutes in 2017-2018. \n") 

        #                                           *-------------- POWER PLAY GOALS AND POINTS -----------------*

        elif StatChosen == 6:

            NMPowerPGdata = datajson ['data'][4]['ppGoals']
            NMPPPdata = datajson ['data'][4]['ppPoints']
            writeHTML( "Nathan MacKinnon had " + str(NMPowerPGdata) + " Power Play Goals and " + str(NMPPPdata) + " Power Play Points in 2017-2018. \n")     

        #                                           *-------------- SHORTHANDED GOALS AND POINTS -----------------*

        elif StatChosen == 7:

            NMSGdata = datajson ['data'][4]['shGoals']
            NMSPdata = datajson ['data'][4]['shPoints']
            writeHTML( "Nathan MacKinnon had " + str(NMSGdata) + " Shorthanded Goals and " + str(NMSPdata) + " Shorthanded Points in 2017-2018. \n")

        #                                           *-------------- FACEOFF PERCENTAGE/SHOTS/SHOOTING PERCENTGE -----------------*

        elif StatChosen == 8:

            NMFcePcgdata = datajson ['data'][4]['faceoffWinPctg']
            NMSdata = datajson ['data'][4]['shots']
            NMShtPcgdata = datajson ['data'][4]['shootingPctg']
            writeHTML( "Nathan MacKinnon had a " + str(NMFcePcgdata) + " Faceoff Percentage, " + str(NMSdata) + " Shots and a " + str(NMShtPcgdata) + " Shooting Percentage in 2017-2018. \n")

        #                                           *-------------- SHIFTS PER GAME AND ICE TIME -----------------*

        elif StatChosen == 9:

            NMSPGdata = datajson ['data'][4]['shiftsPerGame']
            NMTIPGdata = datajson ['data'][4]['timeOnIcePerGame']
            writeHTML( "Nathan MacKinnon had " + str(NMSPGdata) + " Shifts Per Game and " + str(NMTIPGdata) + " seconds on the ice per game in 2017-2018. \n")

        #                                           *-------------- PERSONAL INFO -----------------*

        elif StatChosen == 10:

            NMBDdata = datajson ['data'][4]['playerBirthDate']
            NMBCitydata = datajson ['data'][4]['playerBirthCity']
            NMBPdata = datajson ['data'][4]['playerBirthStateProvince']
            NMBCdata = datajson ['data'][4]['playerBirthCountry']
            NMNdata = datajson ['data'][4]['playerNationality']
            writeHTML( "Nathan MacKinnon was born on " + str(NMBDdata) + " in the city of " + str(NMBCitydata) + ", " + str(NMBPdata) + ", " + str(NMBCdata) + ". His nationality is " + str(NMNdata) + ". \n")

        #                                           *-------------- DRAFT PICK INFO -----------------*

        elif StatChosen == 11:

            NMDOPNdata = datajson ['data'][4]['playerDraftOverallPickNo']
            NMRNdata = datajson ['data'][4]['playerDraftRoundNo']
            NMDYdata = datajson ['data'][4]['playerDraftYear']
            writeHTML( "Nathan MacKinnon was drafted #" + str(NMDOPNdata) + " overall, in the #" + str(NMRNdata) + " round, in year " + str(NMDYdata) + ". \n") 

        #                                           *-------------- HEIGHT AND WEIGHT -----------------*

        elif StatChosen == 12:

            NMHdata = datajson ['data'][4]['playerHeight']
            NMWdata = datajson ['data'][4]['playerWeight']
            writeHTML( "Nathan MacKinnon is " + str(NMHdata) + " inches tall and weighs " + str(NMWdata) + " pounds. \n")

        #                                           *-------------- POSITION/SHOOTS/TEAM -----------------*

        elif StatChosen == 13:

            NMPosdata = datajson ['data'][4]['playerPositionCode']
            NMSdata = datajson ['data'][4]['playerShootsCatches']
            NMTdata = datajson ['data'][4]['playerTeamsPlayedFor']
            writeHTML( "Nathan MacKinnon plays " + str(NMPosdata) + "enter, Shoots " + str(NMSdata) + "ight, and played for " + str(NMTdata) + " in 2017-2018. \n")

        else:
            print("ERROR PLEASE TRY AGAIN")



















                                    #*********************** KUCHEROV ***********************

    elif ItemChosen == 6:

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

        StatChosen = int(input("Please make your selection. \n"))

        #                                           *--------------  GAMES PLAYED -----------------*

        if StatChosen == 1:

            NKGPdata = datajson ['data'][2]['gamesPlayed']
            writeHTML( "Nikita Kucherov had " + str(NKGPdata) + " Games Played in 2017-2018. \n")

        #                                           *-------------- GOALS, ASSISTS, POINTS, POINTS PER GAME -----------------*

        elif StatChosen == 2:

            NKGdata = datajson ['data'][2]['goals']
            NKAdata = datajson ['data'][2]['assists']
            NKPdata = datajson ['data'][2]['points']
            NKPPGdata = datajson ['data'][2]['pointsPerGame']
            writeHTML( "Nikita Kucherov had " + str(NKGdata) + " Goals, " + str(NKAdata) + " Assists, " + str(NKPdata) + " Points and " + str(NKPPGdata)+ " Points Per Game in 2017-2018. \n")

        #                                           *-------------- GAME WINNING GOALS -----------------*

        elif StatChosen == 3:

            NKGWGdata = datajson ['data'][2]['gameWinningGoals']
            writeHTML( "Nikita Kucherov had " + str(NKGWGdata) + " Game Winning Goals in 2017-2018. \n")

        #                                           *-------------- PLUS/MINUS -----------------*

        elif StatChosen == 4:

            NKPlusMdata = datajson ['data'][2]['plusMinus']
            writeHTML( "Nikita Kucherov had a " + str(NKPlusMdata) + " Plus/Minus in 2017-2018. \n")        
        
        #                                           *-------------- PENALTY MINUTES -----------------*

        elif StatChosen == 5:

            NKPMdata = datajson ['data'][2]['penaltyMinutes']
            writeHTML( "Nikita Kucherov had a " + str(NKPMdata) + " Penalty Minutes in 2017-2018. \n") 

        #                                           *-------------- POWER PLAY GOALS AND POINTS -----------------*

        elif StatChosen == 6:

            NKPowerPGdata = datajson ['data'][2]['ppGoals']
            NKPPPdata = datajson ['data'][2]['ppPoints']
            writeHTML( "Nikita Kucherov had " + str(NKPowerPGdata) + " Power Play Goals and " + str(NKPPPdata) + " Power Play Points in 2017-2018. \n")     

        #                                           *-------------- SHORTHANDED GOALS AND POINTS -----------------*

        elif StatChosen == 7:

            NKSGdata = datajson ['data'][2]['shGoals']
            NKSPdata = datajson ['data'][2]['shPoints']
            writeHTML( "Nikita Kucherov had " + str(NKSGdata) + " Shorthanded Goals and " + str(NKSPdata) + " Shorthanded Points in 2017-2018. \n")

        #                                           *-------------- FACEOFF PERCENTAGE/SHOTS/SHOOTING PERCENTGE -----------------*

        elif StatChosen == 8:

            NKFcePcgdata = datajson ['data'][2]['faceoffWinPctg']
            NKSdata = datajson ['data'][2]['shots']
            NKShtPcgdata = datajson ['data'][2]['shootingPctg']
            writeHTML( "Nikita Kucherov had a " + str(NKFcePcgdata) + " Faceoff Percentage, " + str(NKSdata) + " Shots and a " + str(NKShtPcgdata) + " Shooting Percentage in 2017-2018. \n")

        #                                           *-------------- SHIFTS PER GAME AND ICE TIME -----------------*

        elif StatChosen == 9:

            NKSPGdata = datajson ['data'][2]['shiftsPerGame']
            NKTIPGdata = datajson ['data'][2]['timeOnIcePerGame']
            writeHTML( "Nikita Kucherov had " + str(NKSPGdata) + " Shifts Per Game and " + str(NKTIPGdata) + " seconds on the ice per game in 2017-2018. \n")

        #                                           *-------------- PERSONAL INFO -----------------*

        elif StatChosen == 10:

            NKBDdata = datajson ['data'][2]['playerBirthDate']
            NKBCitydata = datajson ['data'][2]['playerBirthCity']
            NKBPdata = datajson ['data'][2]['playerBirthStateProvince']
            NKBCdata = datajson ['data'][2]['playerBirthCountry']
            NKNdata = datajson ['data'][2]['playerNationality']
            writeHTML( "Nikita Kucherov was born on " + str(NKBDdata) + " in the city of " + str(NKBCitydata) + ", " + str(NKBPdata) + ", " + str(NKBCdata) + ". His nationality is " + str(NKNdata) + ". \n")

        #                                           *-------------- DRAFT PICK INFO -----------------*

        elif StatChosen == 11:

            NKDOPNdata = datajson ['data'][2]['playerDraftOverallPickNo']
            NKRNdata = datajson ['data'][2]['playerDraftRoundNo']
            NKDYdata = datajson ['data'][2]['playerDraftYear']
            writeHTML( "Nikita Kucherov was drafted #" + str(NKDOPNdata) + " overall, in the #" + str(NKRNdata) + " round, in year " + str(NKDYdata) + ". \n") 

        #                                           *-------------- HEIGHT AND WEIGHT -----------------*

        elif StatChosen == 12:

            NKHdata = datajson ['data'][2]['playerHeight']
            NKWdata = datajson ['data'][2]['playerWeight']
            writeHTML( "Nikita Kucherov is " + str(NKHdata) + " inches tall and weighs " + str(NKWdata) + " pounds. \n")

        #                                           *-------------- POSITION/SHOOTS/TEAM -----------------*

        elif StatChosen == 13:

            NKPosdata = datajson ['data'][2]['playerPositionCode']
            NKSdata = datajson ['data'][2]['playerShootsCatches']
            NKTdata = datajson ['data'][2]['playerTeamsPlayedFor']
            writeHTML( "Nikita Kucherov plays " + str(NKPosdata) + "ight Wing, Shoots " + str(NKSdata) + "eft, and played for " + str(NKTdata) + " in 2017-2018. \n")

        else:
            print("ERROR PLEASE TRY AGAIN")





















                                    #*********************** OVECHKIN ***********************

    elif ItemChosen == 7:

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

        StatChosen = int(input("Please make your selection. \n"))

        #                                           *--------------  GAMES PLAYED -----------------*

        if StatChosen == 1:

            AOGPdata = datajson ['data'][10]['gamesPlayed']
            writeHTML( "Alexander Ovechkin had " + str(AOGPdata) + " Games Played in 2017-2018. \n")

        #                                           *-------------- GOALS, ASSISTS, POINTS, POINTS PER GAME -----------------*

        elif StatChosen == 2:

            AOGdata = datajson ['data'][10]['goals']
            AOAdata = datajson ['data'][10]['assists']
            AOPdata = datajson ['data'][10]['points']
            AOPPGdata = datajson ['data'][10]['pointsPerGame']
            writeHTML( "Alexander Ovechkin had " + str(AOGdata) + " Goals, " + str(AOAdata) + " Assists, " + str(AOPdata) + " Points and " + str(AOPPGdata)+ " Points Per Game in 2017-2018. \n")

        #                                           *-------------- GAME WINNING GOALS -----------------*

        elif StatChosen == 3:

            AOGWGdata = datajson ['data'][10]['gameWinningGoals']
            writeHTML( "Alexander Ovechkin had " + str(AOGWGdata) + " Game Winning Goals in 2017-2018. \n")

        #                                           *-------------- PLUS/MINUS -----------------*

        elif StatChosen == 4:

            AOPlusMdata = datajson ['data'][10]['plusMinus']
            writeHTML( "Alexander Ovechkin had a " + str(AOPlusMdata) + " Plus/Minus in 2017-2018. \n")        
        
        #                                           *-------------- PENALTY MINUTES -----------------*

        elif StatChosen == 5:

            AOPMdata = datajson ['data'][10]['penaltyMinutes']
            writeHTML( "Alexander Ovechkin had a " + str(AOPMdata) + " Penalty Minutes in 2017-2018. \n") 

        #                                           *-------------- POWER PLAY GOALS AND POINTS -----------------*

        elif StatChosen == 6:

            AOPowerPGdata = datajson ['data'][10]['ppGoals']
            AOPPPdata = datajson ['data'][10]['ppPoints']
            writeHTML( "Alexander Ovechkin had " + str(AOPowerPGdata) + " Power Play Goals and " + str(AOPPPdata) + " Power Play Points in 2017-2018. \n")     

        #                                           *-------------- SHORTHANDED GOALS AND POINTS -----------------*

        elif StatChosen == 7:

            AOSGdata = datajson ['data'][10]['shGoals']
            AOSPdata = datajson ['data'][10]['shPoints']
            writeHTML( "Alexander Ovechkin had " + str(AOSGdata) + " Shorthanded Goals and " + str(AOSPdata) + " Shorthanded Points in 2017-2018. \n")

        #                                           *-------------- FACEOFF PERCENTAGE/SHOTS/SHOOTING PERCENTGE -----------------*

        elif StatChosen == 8:

            AOFcePcgdata = datajson ['data'][10]['faceoffWinPctg']
            AOSdata = datajson ['data'][10]['shots']
            AOShtPcgdata = datajson ['data'][10]['shootingPctg']
            writeHTML( "Alexander Ovechkin had a " + str(AOFcePcgdata) + " Faceoff Percentage, " + str(AOSdata) + " Shots and a " + str(AOShtPcgdata) + " Shooting Percentage in 2017-2018. \n")

        #                                           *-------------- SHIFTS PER GAME AND ICE TIME -----------------*

        elif StatChosen == 9:

            AOSPGdata = datajson ['data'][10]['shiftsPerGame']
            AOTIPGdata = datajson ['data'][10]['timeOnIcePerGame']
            writeHTML( "Alexander Ovechkin had " + str(AOSPGdata) + " Shifts Per Game and " + str(AOTIPGdata) + " seconds on the ice per game in 2017-2018. \n")

        #                                           *-------------- PERSONAL INFO -----------------*

        elif StatChosen == 10:

            AOBDdata = datajson ['data'][10]['playerBirthDate']
            AOBCitydata = datajson ['data'][10]['playerBirthCity']
            AOBPdata = datajson ['data'][10]['playerBirthStateProvince']
            AOBCdata = datajson ['data'][10]['playerBirthCountry']
            AONdata = datajson ['data'][10]['playerNationality']
            writeHTML( "Alexander Ovechkin was born on " + str(AOBDdata) + " in the city of " + str(AOBCitydata) + ", " + str(AOBPdata) + ", " + str(AOBCdata) + ". His nationality is " + str(AONdata) + ". \n")

        #                                           *-------------- DRAFT PICK INFO -----------------*

        elif StatChosen == 11:

            AODOPNdata = datajson ['data'][10]['playerDraftOverallPickNo']
            AORNdata = datajson ['data'][10]['playerDraftRoundNo']
            AODYdata = datajson ['data'][10]['playerDraftYear']
            writeHTML( "Alexander Ovechkin was drafted #" + str(AODOPNdata) + " overall, in the #" + str(AORNdata) + " round, in year " + str(AODYdata) + ". \n") 

        #                                           *-------------- HEIGHT AND WEIGHT -----------------*

        elif StatChosen == 12:

            AOHdata = datajson ['data'][10]['playerHeight']
            AOWdata = datajson ['data'][10]['playerWeight']
            writeHTML( "Alexander Ovechkin is " + str(AOHdata) + " inches tall and weighs " + str(AOWdata) + " pounds. \n")

        #                                           *-------------- POSITION/SHOOTS/TEAM -----------------*

        elif StatChosen == 13:

            AOPosdata = datajson ['data'][10]['playerPositionCode']
            AOSdata = datajson ['data'][10]['playerShootsCatches']
            AOTdata = datajson ['data'][10]['playerTeamsPlayedFor']
            writeHTML( "Alexander Ovechkin plays " + str(AOPosdata) + "eft Wing, Shoots " + str(AOSdata) + "ight, and played for " + str(AOTdata) + " in 2017-2018. \n")

        else:
            print("ERROR PLEASE TRY AGAIN")























                                    #*********************** KANE ***********************

    elif ItemChosen == 8:

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

        StatChosen = int(input("Please make your selection. \n"))

        #                                           *--------------  GAMES PLAYED -----------------*

        if StatChosen == 1:

            PKGPdata = datajson ['data'][27]['gamesPlayed']
            writeHTML( "Patrick Kane had " + str(PKGPdata) + " Games Played in 2017-2018. \n")

        #                                           *-------------- GOALS, ASSISTS, POINTS, POINTS PER GAME -----------------*

        elif StatChosen == 2:

            PKGdata = datajson ['data'][27]['goals']
            PKAdata = datajson ['data'][27]['assists']
            PKPdata = datajson ['data'][27]['points']
            PKPPGdata = datajson ['data'][27]['pointsPerGame']
            writeHTML( "Patrick Kane had " + str(PKGdata) + " Goals, " + str(PKAdata) + " Assists, " + str(PKPdata) + " Points and " + str(PKPPGdata)+ " Points Per Game in 2017-2018. \n")

        #                                           *-------------- GAME WINNING GOALS -----------------*

        elif StatChosen == 3:

            PKGWGdata = datajson ['data'][27]['gameWinningGoals']
            writeHTML( "Patrick Kane had " + str(PKGWGdata) + " Game Winning Goals in 2017-2018. \n")

        #                                           *-------------- PLUS/MINUS -----------------*

        elif StatChosen == 4:

            PKPlusMdata = datajson ['data'][27]['plusMinus']
            writeHTML( "Patrick Kane had a " + str(PKPlusMdata) + " Plus/Minus in 2017-2018. \n")        
        
        #                                           *-------------- PENALTY MINUTES -----------------*

        elif StatChosen == 5:

            PKPMdata = datajson ['data'][27]['penaltyMinutes']
            writeHTML( "Patrick Kane had a " + str(PKPMdata) + " Penalty Minutes in 2017-2018. \n") 

        #                                           *-------------- POWER PLAY GOALS AND POINTS -----------------*

        elif StatChosen == 6:

            PKPowerPGdata = datajson ['data'][27]['ppGoals']
            PKPPPdata = datajson ['data'][27]['ppPoints']
            writeHTML( "Patrick Kane had " + str(PKPowerPGdata) + " Power Play Goals and " + str(PKPPPdata) + " Power Play Points in 2017-2018. \n")     

        #                                           *-------------- SHORTHANDED GOALS AND POINTS -----------------*

        elif StatChosen == 7:

            PKSGdata = datajson ['data'][27]['shGoals']
            PKSPdata = datajson ['data'][27]['shPoints']
            writeHTML( "Patrick Kane had " + str(PKSGdata) + " Shorthanded Goals and " + str(PKSPdata) + " Shorthanded Points in 2017-2018. \n")

        #                                           *-------------- FACEOFF PERCENTAGE/SHOTS/SHOOTING PERCENTGE -----------------*

        elif StatChosen == 8:

            PKFcePcgdata = datajson ['data'][27]['faceoffWinPctg']
            PKSdata = datajson ['data'][27]['shots']
            PKShtPcgdata = datajson ['data'][27]['shootingPctg']
            writeHTML( "Patrick Kane had a " + str(PKFcePcgdata) + " Faceoff Percentage, " + str(PKSdata) + " Shots and a " + str(PKShtPcgdata) + " Shooting Percentage in 2017-2018. \n")

        #                                           *-------------- SHIFTS PER GAME AND ICE TIME -----------------*

        elif StatChosen == 9:

            PKSPGdata = datajson ['data'][27]['shiftsPerGame']
            PKTIPGdata = datajson ['data'][27]['timeOnIcePerGame']
            writeHTML( "Patrick Kane had " + str(PKSPGdata) + " Shifts Per Game and " + str(PKTIPGdata) + " seconds on the ice per game in 2017-2018. \n")

        #                                           *-------------- PERSONAL INFO -----------------*

        elif StatChosen == 10:

            PKBDdata = datajson ['data'][27]['playerBirthDate']
            PKBCitydata = datajson ['data'][27]['playerBirthCity']
            PKBPdata = datajson ['data'][27]['playerBirthStateProvince']
            PKBCdata = datajson ['data'][27]['playerBirthCountry']
            PKNdata = datajson ['data'][27]['playerNationality']
            writeHTML( "Patrick Kane was born on " + str(PKBDdata) + " in the city of " + str(PKBCitydata) + ", " + str(PKBPdata) + ", " + str(PKBCdata) + ". His nationality is " + str(PKNdata) + ". \n")

        #                                           *-------------- DRAFT PICK INFO -----------------*

        elif StatChosen == 11:

            PKDOPNdata = datajson ['data'][27]['playerDraftOverallPickNo']
            PKRNdata = datajson ['data'][27]['playerDraftRoundNo']
            PKDYdata = datajson ['data'][27]['playerDraftYear']
            writeHTML( "Patrick Kane was drafted #" + str(PKDOPNdata) + " overall, in the #" + str(PKRNdata) + " round, in year " + str(PKDYdata) + ". \n") 

        #                                           *-------------- HEIGHT AND WEIGHT -----------------*

        elif StatChosen == 12:

            PKHdata = datajson ['data'][27]['playerHeight']
            PKWdata = datajson ['data'][27]['playerWeight']
            writeHTML( "Patrick Kane is " + str(PKHdata) + " inches tall and weighs " + str(PKWdata) + " pounds. \n")

        #                                           *-------------- POSITION/SHOOTS/TEAM -----------------*

        elif StatChosen == 13:

            PKPosdata = datajson ['data'][27]['playerPositionCode']
            PKSdata = datajson ['data'][27]['playerShootsCatches']
            PKTdata = datajson ['data'][27]['playerTeamsPlayedFor']
            writeHTML( "Patrick Kane plays " + str(PKPosdata) + "enter, Shoots " + str(PKSdata) + "ight, and played for " + str(PKTdata) + " in 2017-2018. \n")

        else:
            print("ERROR PLEASE TRY AGAIN")






















                                    #*********************** NYLANDER ***********************

    elif ItemChosen == 9:

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

        StatChosen = int(input("Please make your selection. \n"))

        #                                           *--------------  GAMES PLAYED -----------------*

        if StatChosen == 1:

            WNGPdata = datajson ['data'][69]['gamesPlayed']
            writeHTML( "William Nylander had " + str(WNGPdata) + " Games Played in 2017-2018. \n")

        #                                           *-------------- GOALS, ASSISTS, POINTS, POINTS PER GAME -----------------*

        elif StatChosen == 2:

            WNGdata = datajson ['data'][69]['goals']
            WNAdata = datajson ['data'][69]['assists']
            WNPdata = datajson ['data'][69]['points']
            WNPPGdata = datajson ['data'][69]['pointsPerGame']
            writeHTML( "William Nylander had " + str(WNGdata) + " Goals, " + str(WNAdata) + " Assists, " + str(WNPdata) + " Points and " + str(WNPPGdata)+ " Points Per Game in 2017-2018. \n")

        #                                           *-------------- GAME WINNING GOALS -----------------*

        elif StatChosen == 3:

            WNGWGdata = datajson ['data'][69]['gameWinningGoals']
            writeHTML( "William Nylander had " + str(WNGWGdata) + " Game Winning Goals in 2017-2018. \n")

        #                                           *-------------- PLUS/MINUS -----------------*

        elif StatChosen == 4:

            WNPlusMdata = datajson ['data'][69]['plusMinus']
            writeHTML( "William Nylander had a " + str(WNPlusMdata) + " Plus/Minus in 2017-2018. \n")        
        
        #                                           *-------------- PENALTY MINUTES -----------------*

        elif StatChosen == 5:

            WNPMdata = datajson ['data'][69]['penaltyMinutes']
            writeHTML( "William Nylander had a " + str(WNPMdata) + " Penalty Minutes in 2017-2018. \n") 

        #                                           *-------------- POWER PLAY GOALS AND POINTS -----------------*

        elif StatChosen == 6:

            WNPowerPGdata = datajson ['data'][69]['ppGoals']
            WNPPPdata = datajson ['data'][69]['ppPoints']
            writeHTML( "William Nylander had " + str(WNPowerPGdata) + " Power Play Goals and " + str(WNPPPdata) + " Power Play Points in 2017-2018. \n")     

        #                                           *-------------- SHORTHANDED GOALS AND POINTS -----------------*

        elif StatChosen == 7:

            WNSGdata = datajson ['data'][69]['shGoals']
            WNSPdata = datajson ['data'][69]['shPoints']
            writeHTML( "William Nylander had " + str(WNSGdata) + " Shorthanded Goals and " + str(WNSPdata) + " Shorthanded Points in 2017-2018. \n")

        #                                           *-------------- FACEOFF PERCENTAGE/SHOTS/SHOOTING PERCENTGE -----------------*

        elif StatChosen == 8:

            WNFcePcgdata = datajson ['data'][69]['faceoffWinPctg']
            WNSdata = datajson ['data'][69]['shots']
            WNShtPcgdata = datajson ['data'][69]['shootingPctg']
            writeHTML( "William Nylander had a " + str(WNFcePcgdata) + " Faceoff Percentage, " + str(WNSdata) + " Shots and a " + str(WNShtPcgdata) + " Shooting Percentage in 2017-2018. \n")

        #                                           *-------------- SHIFTS PER GAME AND ICE TIME -----------------*

        elif StatChosen == 9:

            WNSPGdata = datajson ['data'][69]['shiftsPerGame']
            WNTIPGdata = datajson ['data'][69]['timeOnIcePerGame']
            writeHTML( "William Nylander had " + str(WNSPGdata) + " Shifts Per Game and " + str(WNTIPGdata) + " seconds on the ice per game in 2017-2018. \n")

        #                                           *-------------- PERSONAL INFO -----------------*

        elif StatChosen == 10:

            WNBDdata = datajson ['data'][69]['playerBirthDate']
            WNBCitydata = datajson ['data'][69]['playerBirthCity']
            WNBPdata = datajson ['data'][69]['playerBirthStateProvince']
            WNBCdata = datajson ['data'][69]['playerBirthCountry']
            WNNdata = datajson ['data'][69]['playerNationality']
            writeHTML( "William Nylander was born on " + str(WNBDdata) + " in the city of " + str(WNBCitydata) + ", " + str(WNBPdata) + ", " + str(WNBCdata) + ". His nationality is " + str(WNNdata) + ". \n")

        #                                           *-------------- DRAFT PICK INFO -----------------*

        elif StatChosen == 11:

            WNDOPNdata = datajson ['data'][69]['playerDraftOverallPickNo']
            WNRNdata = datajson ['data'][69]['playerDraftRoundNo']
            WNDYdata = datajson ['data'][69]['playerDraftYear']
            writeHTML( "William Nylander was drafted #" + str(WNDOPNdata) + " overall, in the #" + str(WNRNdata) + " round, in year " + str(WNDYdata) + ". \n") 

        #                                           *-------------- HEIGHT AND WEIGHT -----------------*

        elif StatChosen == 12:

            WNHdata = datajson ['data'][69]['playerHeight']
            WNWdata = datajson ['data'][69]['playerWeight']
            writeHTML( "William Nylander is " + str(WNHdata) + " inches tall and weighs " + str(WNWdata) + " pounds. \n")

        #                                           *-------------- POSITION/SHOOTS/TEAM -----------------*

        elif StatChosen == 13:

            WNPosdata = datajson ['data'][69]['playerPositionCode']
            WNSdata = datajson ['data'][69]['playerShootsCatches']
            WNTdata = datajson ['data'][69]['playerTeamsPlayedFor']
            writeHTML( "William Nylander plays " + str(WNPosdata) + "enter, Shoots " + str(WNSdata) + "ight, and played for " + str(WNTdata) + " in 2017-2018. \n")

        else:
            print("ERROR PLEASE TRY AGAIN")




















                                    #*********************** TAVARES ***********************

    elif ItemChosen == 10:

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

        StatChosen = int(input("Please make your selection. \n"))

        #                                           *--------------  GAMES PLAYED -----------------*

        if StatChosen == 1:

            JTGPdata = datajson ['data'][15]['gamesPlayed']
            writeHTML( "John Tavares had " + str(JTGPdata) + " Games Played in 2017-2018. \n")

        #                                           *-------------- GOALS, ASSISTS, POINTS, POINTS PER GAME -----------------*

        elif StatChosen == 2:

            JTGdata = datajson ['data'][15]['goals']
            JTAdata = datajson ['data'][15]['assists']
            JTPdata = datajson ['data'][15]['points']
            JTPPGdata = datajson ['data'][15]['pointsPerGame']
            writeHTML( "John Tavares had " + str(JTGdata) + " Goals, " + str(JTAdata) + " Assists, " + str(JTPdata) + " Points and " + str(JTPPGdata)+ " Points Per Game in 2017-2018. \n")

        #                                           *-------------- GAME WINNING GOALS -----------------*

        elif StatChosen == 3:

            JTGWGdata = datajson ['data'][15]['gameWinningGoals']
            writeHTML( "John Tavares had " + str(JTGWGdata) + " Game Winning Goals in 2017-2018. \n")

        #                                           *-------------- PLUS/MINUS -----------------*

        elif StatChosen == 4:

            JTPlusMdata = datajson ['data'][15]['plusMinus']
            writeHTML( "John Tavares had a " + str(JTPlusMdata) + " Plus/Minus in 2017-2018. \n")        
        
        #                                           *-------------- PENALTY MINUTES -----------------*

        elif StatChosen == 5:

            JTPMdata = datajson ['data'][15]['penaltyMinutes']
            writeHTML( "John Tavares had a " + str(JTPMdata) + " Penalty Minutes in 2017-2018. \n") 

        #                                           *-------------- POWER PLAY GOALS AND POINTS -----------------*

        elif StatChosen == 6:

            JTPowerPGdata = datajson ['data'][15]['ppGoals']
            JTPPPdata = datajson ['data'][15]['ppPoints']
            writeHTML( "John Tavares had " + str(JTPowerPGdata) + " Power Play Goals and " + str(JTPPPdata) + " Power Play Points in 2017-2018. \n")     

        #                                           *-------------- SHORTHANDED GOALS AND POINTS -----------------*

        elif StatChosen == 7:

            JTSGdata = datajson ['data'][15]['shGoals']
            JTSPdata = datajson ['data'][15]['shPoints']
            writeHTML( "John Tavares had " + str(JTSGdata) + " Shorthanded Goals and " + str(JTSPdata) + " Shorthanded Points in 2017-2018. \n")

        #                                           *-------------- FACEOFF PERCENTAGE/SHOTS/SHOOTING PERCENTGE -----------------*

        elif StatChosen == 8:

            JTFcePcgdata = datajson ['data'][15]['faceoffWinPctg']
            JTSdata = datajson ['data'][15]['shots']
            JTShtPcgdata = datajson ['data'][15]['shootingPctg']
            writeHTML( "John Tavares had a " + str(JTFcePcgdata) + " Faceoff Percentage, " + str(JTSdata) + " Shots and a " + str(JTShtPcgdata) + " Shooting Percentage in 2017-2018. \n")

        #                                           *-------------- SHIFTS PER GAME AND ICE TIME -----------------*

        elif StatChosen == 9:

            JTSPGdata = datajson ['data'][15]['shiftsPerGame']
            JTTIPGdata = datajson ['data'][15]['timeOnIcePerGame']
            writeHTML( "John Tavares had " + str(JTSPGdata) + " Shifts Per Game and " + str(JTTIPGdata) + " seconds on the ice per game in 2017-2018. \n")

        #                                           *-------------- PERSONAL INFO -----------------*

        elif StatChosen == 10:

            JTBDdata = datajson ['data'][15]['playerBirthDate']
            JTBCitydata = datajson ['data'][15]['playerBirthCity']
            JTBPdata = datajson ['data'][15]['playerBirthStateProvince']
            JTBCdata = datajson ['data'][15]['playerBirthCountry']
            JTNdata = datajson ['data'][15]['playerNationality']
            writeHTML( "John Tavares was born on " + str(JTBDdata) + " in the city of " + str(JTBCitydata) + ", " + str(JTBPdata) + ", " + str(JTBCdata) + ". His nationality is " + str(JTNdata) + ". \n")

        #                                           *-------------- DRAFT PICK INFO -----------------*

        elif StatChosen == 11:

            JTDOPNdata = datajson ['data'][15]['playerDraftOverallPickNo']
            JTRNdata = datajson ['data'][15]['playerDraftRoundNo']
            JTDYdata = datajson ['data'][15]['playerDraftYear']
            writeHTML( "John Tavares was drafted #" + str(JTDOPNdata) + " overall, in the #" + str(JTRNdata) + " round, in year " + str(JTDYdata) + ". \n") 

        #                                           *-------------- HEIGHT AND WEIGHT -----------------*

        elif StatChosen == 12:

            JTHdata = datajson ['data'][15]['playerHeight']
            JTWdata = datajson ['data'][15]['playerWeight']
            writeHTML( "John Tavares is " + str(JTHdata) + " inches tall and weighs " + str(JTWdata) + " pounds. \n")

        #                                           *-------------- POSITION/SHOOTS/TEAM -----------------*

        elif StatChosen == 13:

            JTPosdata = datajson ['data'][15]['playerPositionCode']
            JTSdata = datajson ['data'][15]['playerShootsCatches']
            JTTdata = datajson ['data'][15]['playerTeamsPlayedFor']
            writeHTML( "John Tavares plays " + str(JTPosdata) + "enter, Shoots " + str(JTSdata) + "eft, and played for " + str(JTTdata) + " in 2017-2018. \n")

        else:
            print("ERROR PLEASE TRY AGAIN")














                                    #*********************** GIROUX ***********************

    elif ItemChosen == 11:

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

        StatChosen = int(input("Please make your selection. \n"))

        #                                           *--------------  GAMES PLAYED -----------------*

        if StatChosen == 1:

            CGGPdata = datajson ['data'][1]['gamesPlayed']
            writeHTML( "Claude Giroux had " + str(CGGPdata) + " Games Played in 2017-2018. \n")

        #                                           *-------------- GOALS, ASSISTS, POINTS, POINTS PER GAME -----------------*

        elif StatChosen == 2:

            CGGdata = datajson ['data'][1]['goals']
            CGAdata = datajson ['data'][1]['assists']
            CGPdata = datajson ['data'][1]['points']
            CGPPGdata = datajson ['data'][1]['pointsPerGame']
            writeHTML( "Claude Giroux had " + str(CGGdata) + " Goals, " + str(CGAdata) + " Assists, " + str(CGPdata) + " Points and " + str(CGPPGdata)+ " Points Per Game in 2017-2018. \n")

        #                                           *-------------- GAME WINNING GOALS -----------------*

        elif StatChosen == 3:

            CGGWGdata = datajson ['data'][1]['gameWinningGoals']
            writeHTML( "Claude Giroux had " + str(CGGWGdata) + " Game Winning Goals in 2017-2018. \n")

        #                                           *-------------- PLUS/MINUS -----------------*

        elif StatChosen == 4:

            CGPlusMdata = datajson ['data'][1]['plusMinus']
            writeHTML( "Claude Giroux had a " + str(CGPlusMdata) + " Plus/Minus in 2017-2018. \n")        
        
        #                                           *-------------- PENALTY MINUTES -----------------*

        elif StatChosen == 5:

            CGPMdata = datajson ['data'][1]['penaltyMinutes']
            writeHTML( "Claude Giroux had a " + str(CGPMdata) + " Penalty Minutes in 2017-2018. \n") 

        #                                           *-------------- POWER PLAY GOALS AND POINTS -----------------*

        elif StatChosen == 6:

            CGPowerPGdata = datajson ['data'][1]['ppGoals']
            CGPPPdata = datajson ['data'][1]['ppPoints']
            writeHTML( "Claude Giroux had " + str(CGPowerPGdata) + " Power Play Goals and " + str(CGPPPdata) + " Power Play Points in 2017-2018. \n")     

        #                                           *-------------- SHORTHANDED GOALS AND POINTS -----------------*

        elif StatChosen == 7:

            CGSGdata = datajson ['data'][1]['shGoals']
            CGSPdata = datajson ['data'][1]['shPoints']
            writeHTML( "Claude Giroux had " + str(CGSGdata) + " Shorthanded Goals and " + str(CGSPdata) + " Shorthanded Points in 2017-2018. \n")

        #                                           *-------------- FACEOFF PERCENTAGE/SHOTS/SHOOTING PERCENTGE -----------------*

        elif StatChosen == 8:

            CGFcePcgdata = datajson ['data'][1]['faceoffWinPctg']
            CGSdata = datajson ['data'][1]['shots']
            CGShtPcgdata = datajson ['data'][1]['shootingPctg']
            writeHTML( "Claude Giroux had a " + str(CGFcePcgdata) + " Faceoff Percentage, " + str(CGSdata) + " Shots and a " + str(CGShtPcgdata) + " Shooting Percentage in 2017-2018. \n")

        #                                           *-------------- SHIFTS PER GAME AND ICE TIME -----------------*

        elif StatChosen == 9:

            CGSPGdata = datajson ['data'][1]['shiftsPerGame']
            CGTIPGdata = datajson ['data'][1]['timeOnIcePerGame']
            writeHTML( "Claude Giroux had " + str(CGSPGdata) + " Shifts Per Game and " + str(CGTIPGdata) + " seconds on the ice per game in 2017-2018. \n")

        #                                           *-------------- PERSONAL INFO -----------------*

        elif StatChosen == 10:

            CGBDdata = datajson ['data'][1]['playerBirthDate']
            CGBCitydata = datajson ['data'][1]['playerBirthCity']
            CGBPdata = datajson ['data'][1]['playerBirthStateProvince']
            CGBCdata = datajson ['data'][1]['playerBirthCountry']
            CGNdata = datajson ['data'][1]['playerNationality']
            writeHTML( "Claude Giroux was born on " + str(CGBDdata) + " in the city of " + str(CGBCitydata) + ", " + str(CGBPdata) + ", " + str(CGBCdata) + ". His nationality is " + str(CGNdata) + ". \n")

        #                                           *-------------- DRAFT PICK INFO -----------------*

        elif StatChosen == 11:

            CGDOPNdata = datajson ['data'][1]['playerDraftOverallPickNo']
            CGRNdata = datajson ['data'][1]['playerDraftRoundNo']
            CGDYdata = datajson ['data'][1]['playerDraftYear']
            writeHTML( "Claude Giroux was drafted #" + str(CGDOPNdata) + " overall, in the #" + str(CGRNdata) + " round, in year " + str(CGDYdata) + ". \n") 

        #                                           *-------------- HEIGHT AND WEIGHT -----------------*

        elif StatChosen == 12:

            CGHdata = datajson ['data'][1]['playerHeight']
            CGWdata = datajson ['data'][1]['playerWeight']
            writeHTML( "Claude Giroux is " + str(CGHdata) + " inches tall and weighs " + str(CGWdata) + " pounds. \n")

        #                                           *-------------- POSITION/SHOOTS/TEAM -----------------*

        elif StatChosen == 13:

            CGPosdata = datajson ['data'][1]['playerPositionCode']
            CGSdata = datajson ['data'][1]['playerShootsCatches']
            CGTdata = datajson ['data'][1]['playerTeamsPlayedFor']
            writeHTML( "Claude Giroux plays " + str(CGPosdata) + "ight Wing, Shoots " + str(CGSdata) + "ight, and played for " + str(CGTdata) + " in 2017-2018. \n")

        else:
            print("ERROR PLEASE TRY AGAIN")
















                                                #*********************** MALKIN ***********************

    elif ItemChosen == 12:

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

        StatChosen = int(input("Please make your selection. \n"))

        #                                           *--------------  GAMES PLAYED -----------------*

        if StatChosen == 1:

            EMGPdata = datajson ['data'][3]['gamesPlayed']
            writeHTML( "Evgeni Malkin had " + str(EMGPdata) + " Games Played in 2017-2018. \n")

        #                                           *-------------- GOALS, ASSISTS, POINTS, POINTS PER GAME -----------------*

        elif StatChosen == 2:

            EMGdata = datajson ['data'][3]['goals']
            EMAdata = datajson ['data'][3]['assists']
            EMPdata = datajson ['data'][3]['points']
            EMPPGdata = datajson ['data'][3]['pointsPerGame']
            writeHTML( "Evgeni Malkin had " + str(EMGdata) + " Goals, " + str(EMAdata) + " Assists, " + str(EMPdata) + " Points and " + str(EMPPGdata)+ " Points Per Game in 2017-2018. \n")

        #                                           *-------------- GAME WINNING GOALS -----------------*

        elif StatChosen == 3:

            EMGWGdata = datajson ['data'][3]['gameWinningGoals']
            writeHTML( "Evgeni Malkin had " + str(EMGWGdata) + " Game Winning Goals in 2017-2018. \n")

        #                                           *-------------- PLUS/MINUS -----------------*

        elif StatChosen == 4:

            EMPlusMdata = datajson ['data'][3]['plusMinus']
            writeHTML( "Evgeni Malkin had a " + str(EMPlusMdata) + " Plus/Minus in 2017-2018. \n")        
        
        #                                           *-------------- PENALTY MINUTES -----------------*

        elif StatChosen == 5:

            EMPMdata = datajson ['data'][3]['penaltyMinutes']
            writeHTML( "Evgeni Malkin had a " + str(EMPMdata) + " Penalty Minutes in 2017-2018. \n") 

        #                                           *-------------- POWER PLAY GOALS AND POINTS -----------------*

        elif StatChosen == 6:

            EMPowerPGdata = datajson ['data'][3]['ppGoals']
            EMPPPdata = datajson ['data'][3]['ppPoints']
            writeHTML( "Evgeni Malkin had " + str(EMPowerPGdata) + " Power Play Goals and " + str(EMPPPdata) + " Power Play Points in 2017-2018. \n")     

        #                                           *-------------- SHORTHANDED GOALS AND POINTS -----------------*

        elif StatChosen == 7:

            EMSGdata = datajson ['data'][3]['shGoals']
            EMSPdata = datajson ['data'][3]['shPoints']
            writeHTML( "Evgeni Malkin had " + str(EMSGdata) + " Shorthanded Goals and " + str(EMSPdata) + " Shorthanded Points in 2017-2018. \n")

        #                                           *-------------- FACEOFF PERCENTAGE/SHOTS/SHOOTING PERCENTGE -----------------*

        elif StatChosen == 8:

            EMFcePcgdata = datajson ['data'][3]['faceoffWinPctg']
            EMSdata = datajson ['data'][3]['shots']
            EMShtPcgdata = datajson ['data'][3]['shootingPctg']
            writeHTML( "Evgeni Malkin had a " + str(EMFcePcgdata) + " Faceoff Percentage, " + str(EMSdata) + " Shots and a " + str(EMShtPcgdata) + " Shooting Percentage in 2017-2018. \n")

        #                                           *-------------- SHIFTS PER GAME AND ICE TIME -----------------*

        elif StatChosen == 9:

            EMSPGdata = datajson ['data'][3]['shiftsPerGame']
            EMTIPGdata = datajson ['data'][3]['timeOnIcePerGame']
            writeHTML( "Evgeni Malkin had " + str(EMSPGdata) + " Shifts Per Game and " + str(EMTIPGdata) + " seconds on the ice per game in 2017-2018. \n")

        #                                           *-------------- PERSONAL INFO -----------------*

        elif StatChosen == 10:

            EMBDdata = datajson ['data'][3]['playerBirthDate']
            EMBCitydata = datajson ['data'][3]['playerBirthCity']
            EMBPdata = datajson ['data'][3]['playerBirthStateProvince']
            EMBCdata = datajson ['data'][3]['playerBirthCountry']
            EMNdata = datajson ['data'][3]['playerNationality']
            writeHTML( "Evgeni Malkin was born on " + str(EMBDdata) + " in the city of " + str(EMBCitydata) + ", " + str(EMBPdata) + ", " + str(EMBCdata) + ". His nationality is " + str(EMNdata) + ". \n")

        #                                           *-------------- DRAFT PICK INFO -----------------*

        elif StatChosen == 11:

            EMDOPNdata = datajson ['data'][3]['playerDraftOverallPickNo']
            EMRNdata = datajson ['data'][3]['playerDraftRoundNo']
            EMDYdata = datajson ['data'][3]['playerDraftYear']
            writeHTML( "Evgeni Malkin was drafted #" + str(EMDOPNdata) + " overall, in the #" + str(EMRNdata) + " round, in year " + str(EMDYdata) + ". \n") 

        #                                           *-------------- HEIGHT AND WEIGHT -----------------*

        elif StatChosen == 12:

            EMHdata = datajson ['data'][3]['playerHeight']
            EMWdata = datajson ['data'][3]['playerWeight']
            writeHTML( "Evgeni Malkin is " + str(EMHdata) + " inches tall and weighs " + str(EMWdata) + " pounds. \n")

        #                                           *-------------- POSITION/SHOOTS/TEAM -----------------*

        elif StatChosen == 13:

            EMPosdata = datajson ['data'][3]['playerPositionCode']
            EMSdata = datajson ['data'][3]['playerShootsCatches']
            EMTdata = datajson ['data'][3]['playerTeamsPlayedFor']
            writeHTML( "Evgeni Malkin plays " + str(EMPosdata) + "enter, Shoots " + str(EMSdata) + "eft, and played for " + str(EMTdata) + " in 2017-2018. \n")

        else:
            print("ERROR PLEASE TRY AGAIN")























                                    #*********************** HALL ***********************

    elif ItemChosen == 13:

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

        StatChosen = int(input("Please make your selection. \n"))

        #                                           *--------------  GAMES PLAYED -----------------*

        if StatChosen == 1:

            THGPdata = datajson ['data'][5]['gamesPlayed']
            writeHTML( "Taylor Hall had " + str(THGPdata) + " Games Played in 2017-2018. \n")

        #                                           *-------------- GOALS, ASSISTS, POINTS, POINTS PER GAME -----------------*

        elif StatChosen == 2:

            THGdata = datajson ['data'][5]['goals']
            THAdata = datajson ['data'][5]['assists']
            THPdata = datajson ['data'][5]['points']
            THPPGdata = datajson ['data'][5]['pointsPerGame']
            writeHTML( "Taylor Hall had " + str(THGdata) + " Goals, " + str(THAdata) + " Assists, " + str(THPdata) + " Points and " + str(THPPGdata)+ " Points Per Game in 2017-2018. \n")

        #                                           *-------------- GAME WINNING GOALS -----------------*

        elif StatChosen == 3:

            THGWGdata = datajson ['data'][5]['gameWinningGoals']
            writeHTML( "Taylor Hall had " + str(THGWGdata) + " Game Winning Goals in 2017-2018. \n")

        #                                           *-------------- PLUS/MINUS -----------------*

        elif StatChosen == 4:

            THPlusMdata = datajson ['data'][5]['plusMinus']
            writeHTML( "Taylor Hall had a " + str(THPlusMdata) + " Plus/Minus in 2017-2018. \n")        
        
        #                                           *-------------- PENALTY MINUTES -----------------*

        elif StatChosen == 5:

            THPMdata = datajson ['data'][5]['penaltyMinutes']
            writeHTML( "Taylor Hall had a " + str(THPMdata) + " Penalty Minutes in 2017-2018. \n") 

        #                                           *-------------- POWER PLAY GOALS AND POINTS -----------------*

        elif StatChosen == 6:

            THPowerPGdata = datajson ['data'][5]['ppGoals']
            THPPPdata = datajson ['data'][5]['ppPoints']
            writeHTML( "Taylor Hall had " + str(THPowerPGdata) + " Power Play Goals and " + str(THPPPdata) + " Power Play Points in 2017-2018. \n")     

        #                                           *-------------- SHORTHANDED GOALS AND POINTS -----------------*

        elif StatChosen == 7:

            THSGdata = datajson ['data'][5]['shGoals']
            THSPdata = datajson ['data'][5]['shPoints']
            writeHTML( "Taylor Hall had " + str(THSGdata) + " Shorthanded Goals and " + str(THSPdata) + " Shorthanded Points in 2017-2018. \n")

        #                                           *-------------- FACEOFF PERCENTAGE/SHOTS/SHOOTING PERCENTGE -----------------*

        elif StatChosen == 8:

            THFcePcgdata = datajson ['data'][5]['faceoffWinPctg']
            THSdata = datajson ['data'][5]['shots']
            THShtPcgdata = datajson ['data'][5]['shootingPctg']
            writeHTML( "Taylor Hall had a " + str(THFcePcgdata) + " Faceoff Percentage, " + str(THSdata) + " Shots and a " + str(THShtPcgdata) + " Shooting Percentage in 2017-2018. \n")

        #                                           *-------------- SHIFTS PER GAME AND ICE TIME -----------------*

        elif StatChosen == 9:

            THSPGdata = datajson ['data'][5]['shiftsPerGame']
            THTIPGdata = datajson ['data'][5]['timeOnIcePerGame']
            writeHTML( "Taylor Hall had " + str(THSPGdata) + " Shifts Per Game and " + str(THTIPGdata) + " seconds on the ice per game in 2017-2018. \n")

        #                                           *-------------- PERSONAL INFO -----------------*

        elif StatChosen == 10:

            THBDdata = datajson ['data'][5]['playerBirthDate']
            THBCitydata = datajson ['data'][5]['playerBirthCity']
            THBPdata = datajson ['data'][5]['playerBirthStateProvince']
            THBCdata = datajson ['data'][5]['playerBirthCountry']
            THNdata = datajson ['data'][5]['playerNationality']
            writeHTML( "Taylor Hall was born on " + str(THBDdata) + " in the city of " + str(THBCitydata) + ", " + str(THBPdata) + ", " + str(THBCdata) + ". His nationality is " + str(THNdata) + ". \n")

        #                                           *-------------- DRAFT PICK INFO -----------------*

        elif StatChosen == 11:

            THDOPNdata = datajson ['data'][5]['playerDraftOverallPickNo']
            THRNdata = datajson ['data'][5]['playerDraftRoundNo']
            THDYdata = datajson ['data'][5]['playerDraftYear']
            writeHTML( "Taylor Hall was drafted #" + str(THDOPNdata) + " overall, in the #" + str(THRNdata) + " round, in year " + str(THDYdata) + ". \n") 

        #                                           *-------------- HEIGHT AND WEIGHT -----------------*

        elif StatChosen == 12:

            THHdata = datajson ['data'][5]['playerHeight']
            THWdata = datajson ['data'][5]['playerWeight']
            writeHTML( "Taylor Hall is " + str(THHdata) + " inches tall and weighs " + str(THWdata) + " pounds. \n")

        #                                           *-------------- POSITION/SHOOTS/TEAM -----------------*

        elif StatChosen == 13:

            THPosdata = datajson ['data'][5]['playerPositionCode']
            THSdata = datajson ['data'][5]['playerShootsCatches']
            THTdata = datajson ['data'][5]['playerTeamsPlayedFor']
            writeHTML( "Taylor Hall plays " + str(THPosdata) + "eft Wing, Shoots " + str(THSdata) + "eft, and played for " + str(THTdata) + " in 2017-2018. \n")

        else:
            print("ERROR PLEASE TRY AGAIN")


















                                    #*********************** KOPITAR ***********************

    elif ItemChosen == 14:

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

        StatChosen = int(input("Please make your selection. \n"))

        #                                           *--------------  GAMES PLAYED -----------------*

        if StatChosen == 1:

            AKGPdata = datajson ['data'][6]['gamesPlayed']
            writeHTML( "Anze Kopitar had " + str(AKGPdata) + " Games Played in 2017-2018. \n")

        #                                           *-------------- GOALS, ASSISTS, POINTS, POINTS PER GAME -----------------*

        elif StatChosen == 2:

            AKGdata = datajson ['data'][6]['goals']
            AKAdata = datajson ['data'][6]['assists']
            AKPdata = datajson ['data'][6]['points']
            AKPPGdata = datajson ['data'][6]['pointsPerGame']
            writeHTML( "Anze Kopitar had " + str(AKGdata) + " Goals, " + str(AKAdata) + " Assists, " + str(AKPdata) + " Points and " + str(AKPPGdata)+ " Points Per Game in 2017-2018. \n")

        #                                           *-------------- GAME WINNING GOALS -----------------*

        elif StatChosen == 3:

            AKGWGdata = datajson ['data'][6]['gameWinningGoals']
            writeHTML( "Anze Kopitar had " + str(AKGWGdata) + " Game Winning Goals in 2017-2018. \n")

        #                                           *-------------- PLUS/MINUS -----------------*

        elif StatChosen == 4:

            AKPlusMdata = datajson ['data'][6]['plusMinus']
            writeHTML( "Anze Kopitar had a " + str(AKPlusMdata) + " Plus/Minus in 2017-2018. \n")        
        
        #                                           *-------------- PENALTY MINUTES -----------------*

        elif StatChosen == 5:

            AKPMdata = datajson ['data'][6]['penaltyMinutes']
            writeHTML( "Anze Kopitar had a " + str(AKPMdata) + " Penalty Minutes in 2017-2018. \n") 

        #                                           *-------------- POWER PLAY GOALS AND POINTS -----------------*

        elif StatChosen == 6:

            AKPowerPGdata = datajson ['data'][6]['ppGoals']
            AKPPPdata = datajson ['data'][6]['ppPoints']
            writeHTML( "Anze Kopitar had " + str(AKPowerPGdata) + " Power Play Goals and " + str(AKPPPdata) + " Power Play Points in 2017-2018. \n")     

        #                                           *-------------- SHORTHANDED GOALS AND POINTS -----------------*

        elif StatChosen == 7:

            AKSGdata = datajson ['data'][6]['shGoals']
            AKSPdata = datajson ['data'][6]['shPoints']
            writeHTML( "Anze Kopitar had " + str(AKSGdata) + " Shorthanded Goals and " + str(AKSPdata) + " Shorthanded Points in 2017-2018. \n")

        #                                           *-------------- FACEOFF PERCENTAGE/SHOTS/SHOOTING PERCENTGE -----------------*

        elif StatChosen == 8:

            AKFcePcgdata = datajson ['data'][6]['faceoffWinPctg']
            AKSdata = datajson ['data'][6]['shots']
            AKShtPcgdata = datajson ['data'][6]['shootingPctg']
            writeHTML( "Anze Kopitar had a " + str(AKFcePcgdata) + " Faceoff Percentage, " + str(AKSdata) + " Shots and a " + str(AKShtPcgdata) + " Shooting Percentage in 2017-2018. \n")

        #                                           *-------------- SHIFTS PER GAME AND ICE TIME -----------------*

        elif StatChosen == 9:

            AKSPGdata = datajson ['data'][6]['shiftsPerGame']
            AKTIPGdata = datajson ['data'][6]['timeOnIcePerGame']
            writeHTML( "Anze Kopitar had " + str(AKSPGdata) + " Shifts Per Game and " + str(AKTIPGdata) + " seconds on the ice per game in 2017-2018. \n")

        #                                           *-------------- PERSONAL INFO -----------------*

        elif StatChosen == 10:

            AKBDdata = datajson ['data'][6]['playerBirthDate']
            AKBCitydata = datajson ['data'][6]['playerBirthCity']
            AKBPdata = datajson ['data'][6]['playerBirthStateProvince']
            AKBCdata = datajson ['data'][6]['playerBirthCountry']
            AKNdata = datajson ['data'][6]['playerNationality']
            writeHTML( "Anze Kopitar was born on " + str(AKBDdata) + " in the city of " + str(AKBCitydata) + ", " + str(AKBPdata) + ", " + str(AKBCdata) + ". His nationality is " + str(AKNdata) + ". \n")

        #                                           *-------------- DRAFT PICK INFO -----------------*

        elif StatChosen == 11:

            AKDOPNdata = datajson ['data'][6]['playerDraftOverallPickNo']
            AKRNdata = datajson ['data'][6]['playerDraftRoundNo']
            AKDYdata = datajson ['data'][6]['playerDraftYear']
            writeHTML( "Anze Kopitar was drafted #" + str(AKDOPNdata) + " overall, in the #" + str(AKRNdata) + " round, in year " + str(AKDYdata) + ". \n") 

        #                                           *-------------- HEIGHT AND WEIGHT -----------------*

        elif StatChosen == 12:

            AKHdata = datajson ['data'][6]['playerHeight']
            AKWdata = datajson ['data'][6]['playerWeight']
            writeHTML( "Anze Kopitar is " + str(AKHdata) + " inches tall and weighs " + str(AKWdata) + " pounds. \n")

        #                                           *-------------- POSITION/SHOOTS/TEAM -----------------*

        elif StatChosen == 13:

            AKPosdata = datajson ['data'][6]['playerPositionCode']
            AKSdata = datajson ['data'][6]['playerShootsCatches']
            AKTdata = datajson ['data'][6]['playerTeamsPlayedFor']
            writeHTML( "Anze Kopitar plays " + str(AKPosdata) + "enter, Shoots " + str(AKSdata) + "eft, and played for " + str(AKTdata) + " in 2017-2018. \n")

        else:
            print("ERROR PLEASE TRY AGAIN")












                                    #*********************** KESSEL ***********************

    elif ItemChosen == 15:

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

        StatChosen = int(input("Please make your selection. \n"))

        #                                           *--------------  GAMES PLAYED -----------------*

        if StatChosen == 1:

            PKGPdata = datajson ['data'][7]['gamesPlayed']
            writeHTML( "Phil Kessel had " + str(PKGPdata) + " Games Played in 2017-2018. \n")

        #                                           *-------------- GOALS, ASSISTS, POINTS, POINTS PER GAME -----------------*

        elif StatChosen == 2:

            PKGdata = datajson ['data'][7]['goals']
            PKAdata = datajson ['data'][7]['assists']
            PKPdata = datajson ['data'][7]['points']
            PKPPGdata = datajson ['data'][7]['pointsPerGame']
            writeHTML( "Phil Kessel had " + str(PKGdata) + " Goals, " + str(PKAdata) + " Assists, " + str(PKPdata) + " Points and " + str(PKPPGdata)+ " Points Per Game in 2017-2018. \n")

        #                                           *-------------- GAME WINNING GOALS -----------------*

        elif StatChosen == 3:

            PKGWGdata = datajson ['data'][7]['gameWinningGoals']
            writeHTML( "Phil Kessel had " + str(PKGWGdata) + " Game Winning Goals in 2017-2018. \n")

        #                                           *-------------- PLUS/MINUS -----------------*

        elif StatChosen == 4:

            PKPlusMdata = datajson ['data'][7]['plusMinus']
            writeHTML( "Phil Kessel had a " + str(PKPlusMdata) + " Plus/Minus in 2017-2018. \n")        
        
        #                                           *-------------- PENALTY MINUTES -----------------*

        elif StatChosen == 5:

            PKPMdata = datajson ['data'][7]['penaltyMinutes']
            writeHTML( "Phil Kessel had a " + str(PKPMdata) + " Penalty Minutes in 2017-2018. \n") 

        #                                           *-------------- POWER PLAY GOALS AND POINTS -----------------*

        elif StatChosen == 6:

            PKPowerPGdata = datajson ['data'][7]['ppGoals']
            PKPPPdata = datajson ['data'][7]['ppPoints']
            writeHTML( "Phil Kessel had " + str(PKPowerPGdata) + " Power Play Goals and " + str(PKPPPdata) + " Power Play Points in 2017-2018. \n")     

        #                                           *-------------- SHORTHANDED GOALS AND POINTS -----------------*

        elif StatChosen == 7:

            PKSGdata = datajson ['data'][7]['shGoals']
            PKSPdata = datajson ['data'][7]['shPoints']
            writeHTML( "Phil Kessel had " + str(PKSGdata) + " Shorthanded Goals and " + str(PKSPdata) + " Shorthanded Points in 2017-2018. \n")

        #                                           *-------------- FACEOFF PERCENTAGE/SHOTS/SHOOTING PERCENTGE -----------------*

        elif StatChosen == 8:

            PKFcePcgdata = datajson ['data'][7]['faceoffWinPctg']
            PKSdata = datajson ['data'][7]['shots']
            PKShtPcgdata = datajson ['data'][7]['shootingPctg']
            writeHTML( "Phil Kessel had a " + str(PKFcePcgdata) + " Faceoff Percentage, " + str(PKSdata) + " Shots and a " + str(PKShtPcgdata) + " Shooting Percentage in 2017-2018. \n")

        #                                           *-------------- SHIFTS PER GAME AND ICE TIME -----------------*

        elif StatChosen == 9:

            PKSPGdata = datajson ['data'][7]['shiftsPerGame']
            PKTIPGdata = datajson ['data'][7]['timeOnIcePerGame']
            writeHTML( "Phil Kessel had " + str(PKSPGdata) + " Shifts Per Game and " + str(PKTIPGdata) + " seconds on the ice per game in 2017-2018. \n")

        #                                           *-------------- PERSONAL INFO -----------------*

        elif StatChosen == 10:

            PKBDdata = datajson ['data'][7]['playerBirthDate']
            PKBCitydata = datajson ['data'][7]['playerBirthCity']
            PKBPdata = datajson ['data'][7]['playerBirthStateProvince']
            PKBCdata = datajson ['data'][7]['playerBirthCountry']
            PKNdata = datajson ['data'][7]['playerNationality']
            writeHTML( "Phil Kessel was born on " + str(PKBDdata) + " in the city of " + str(PKBCitydata) + ", " + str(PKBPdata) + ", " + str(PKBCdata) + ". His nationality is " + str(PKNdata) + ". \n")

        #                                           *-------------- DRAFT PICK INFO -----------------*

        elif StatChosen == 11:

            PKDOPNdata = datajson ['data'][7]['playerDraftOverallPickNo']
            PKRNdata = datajson ['data'][7]['playerDraftRoundNo']
            PKDYdata = datajson ['data'][7]['playerDraftYear']
            writeHTML( "Phil Kessel was drafted #" + str(PKDOPNdata) + " overall, in the #" + str(PKRNdata) + " round, in year " + str(PKDYdata) + ". \n") 

        #                                           *-------------- HEIGHT AND WEIGHT -----------------*

        elif StatChosen == 12:

            PKHdata = datajson ['data'][7]['playerHeight']
            PKWdata = datajson ['data'][7]['playerWeight']
            writeHTML( "Phil Kessel is " + str(PKHdata) + " inches tall and weighs " + str(PKWdata) + " pounds. \n")

        #                                           *-------------- POSITION/SHOOTS/TEAM -----------------*

        elif StatChosen == 13:

            PKPosdata = datajson ['data'][7]['playerPositionCode']
            PKSdata = datajson ['data'][7]['playerShootsCatches']
            PKTdata = datajson ['data'][7]['playerTeamsPlayedFor']
            writeHTML( "Phil Kessel plays " + str(PKPosdata) + "enter, Shoots " + str(PKSdata) + "ight, and played for " + str(PKTdata) + " in 2017-2018. \n")

        else:
            print("ERROR PLEASE TRY AGAIN")











                                    #*********************** WHEELER ***********************

    elif ItemChosen == 16:

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

        StatChosen = int(input("Please make your selection. \n"))

        #                                           *--------------  GAMES PLAYED -----------------*

        if StatChosen == 1:

            BWGPdata = datajson ['data'][8]['gamesPlayed']
            writeHTML( "Blake Wheeler had " + str(BWGPdata) + " Games Played in 2017-2018. \n")

        #                                           *-------------- GOALS, ASSISTS, POINTS, POINTS PER GAME -----------------*

        elif StatChosen == 2:

            BWGdata = datajson ['data'][8]['goals']
            BWAdata = datajson ['data'][8]['assists']
            BWPdata = datajson ['data'][8]['points']
            BWPPGdata = datajson ['data'][8]['pointsPerGame']
            writeHTML( "Blake Wheeler had " + str(BWGdata) + " Goals, " + str(BWAdata) + " Assists, " + str(BWPdata) + " Points and " + str(BWPPGdata)+ " Points Per Game in 2017-2018. \n")

        #                                           *-------------- GAME WINNING GOALS -----------------*

        elif StatChosen == 3:

            BWGWGdata = datajson ['data'][8]['gameWinningGoals']
            writeHTML( "Blake Wheeler had " + str(BWGWGdata) + " Game Winning Goals in 2017-2018. \n")

        #                                           *-------------- PLUS/MINUS -----------------*

        elif StatChosen == 4:

            BWPlusMdata = datajson ['data'][8]['plusMinus']
            writeHTML( "Blake Wheeler had a " + str(BWPlusMdata) + " Plus/Minus in 2017-2018. \n")        
        
        #                                           *-------------- PENALTY MINUTES -----------------*

        elif StatChosen == 5:

            BWPMdata = datajson ['data'][8]['penaltyMinutes']
            writeHTML( "Blake Wheeler had a " + str(BWPMdata) + " Penalty Minutes in 2017-2018. \n") 

        #                                           *-------------- POWER PLAY GOALS AND POINTS -----------------*

        elif StatChosen == 6:

            BWPowerPGdata = datajson ['data'][8]['ppGoals']
            BWPPPdata = datajson ['data'][8]['ppPoints']
            writeHTML( "Blake Wheeler had " + str(BWPowerPGdata) + " Power Play Goals and " + str(BWPPPdata) + " Power Play Points in 2017-2018. \n")     

        #                                           *-------------- SHORTHANDED GOALS AND POINTS -----------------*

        elif StatChosen == 7:

            BWSGdata = datajson ['data'][8]['shGoals']
            BWSPdata = datajson ['data'][8]['shPoints']
            writeHTML( "Blake Wheeler had " + str(BWSGdata) + " Shorthanded Goals and " + str(BWSPdata) + " Shorthanded Points in 2017-2018. \n")

        #                                           *-------------- FACEOFF PERCENTAGE/SHOTS/SHOOTING PERCENTGE -----------------*

        elif StatChosen == 8:

            BWFcePcgdata = datajson ['data'][8]['faceoffWinPctg']
            BWSdata = datajson ['data'][8]['shots']
            BWShtPcgdata = datajson ['data'][8]['shootingPctg']
            writeHTML( "Blake Wheeler had a " + str(BWFcePcgdata) + " Faceoff Percentage, " + str(BWSdata) + " Shots and a " + str(BWShtPcgdata) + " Shooting Percentage in 2017-2018. \n")

        #                                           *-------------- SHIFTS PER GAME AND ICE TIME -----------------*

        elif StatChosen == 9:

            BWSPGdata = datajson ['data'][8]['shiftsPerGame']
            BWTIPGdata = datajson ['data'][8]['timeOnIcePerGame']
            writeHTML( "Blake Wheeler had " + str(BWSPGdata) + " Shifts Per Game and " + str(BWTIPGdata) + " seconds on the ice per game in 2017-2018. \n")

        #                                           *-------------- PERSONAL INFO -----------------*

        elif StatChosen == 10:

            BWBDdata = datajson ['data'][8]['playerBirthDate']
            BWBCitydata = datajson ['data'][8]['playerBirthCity']
            BWBPdata = datajson ['data'][8]['playerBirthStateProvince']
            BWBCdata = datajson ['data'][8]['playerBirthCountry']
            BWNdata = datajson ['data'][8]['playerNationality']
            writeHTML( "Blake Wheeler was born on " + str(BWBDdata) + " in the city of " + str(BWBCitydata) + ", " + str(BWBPdata) + ", " + str(BWBCdata) + ". His nationality is " + str(BWNdata) + ". \n")

        #                                           *-------------- DRAFT PICK INFO -----------------*

        elif StatChosen == 11:

            BWDOPNdata = datajson ['data'][8]['playerDraftOverallPickNo']
            BWRNdata = datajson ['data'][8]['playerDraftRoundNo']
            BWDYdata = datajson ['data'][8]['playerDraftYear']
            writeHTML( "Blake Wheeler was drafted #" + str(BWDOPNdata) + " overall, in the #" + str(BWRNdata) + " round, in year " + str(BWDYdata) + ". \n") 

        #                                           *-------------- HEIGHT AND WEIGHT -----------------*

        elif StatChosen == 12:

            BWHdata = datajson ['data'][8]['playerHeight']
            BWWdata = datajson ['data'][8]['playerWeight']
            writeHTML( "Blake Wheeler is " + str(BWHdata) + " inches tall and weighs " + str(BWWdata) + " pounds. \n")

        #                                           *-------------- POSITION/SHOOTS/TEAM -----------------*

        elif StatChosen == 13:

            BWPosdata = datajson ['data'][8]['playerPositionCode']
            BWSdata = datajson ['data'][8]['playerShootsCatches']
            BWTdata = datajson ['data'][8]['playerTeamsPlayedFor']
            writeHTML( "Blake Wheeler plays " + str(BWPosdata) + "ight Wing, Shoots " + str(BWSdata) + "ight, and played for " + str(BWTdata) + " in 2017-2018. \n")

        else:
            print("ERROR PLEASE TRY AGAIN")








                                    #*********************** STAMKOS ***********************

    elif ItemChosen == 17:

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

        StatChosen = int(input("Please make your selection. \n"))

        #                                           *--------------  GAMES PLAYED -----------------*

        if StatChosen == 1:

            SSGPdata = datajson ['data'][11]['gamesPlayed']
            writeHTML( "Steven Stamkos had " + str(SSGPdata) + " Games Played in 2017-2018. \n")

        #                                           *-------------- GOALS, ASSISTS, POINTS, POINTS PER GAME -----------------*

        elif StatChosen == 2:

            SSGdata = datajson ['data'][11]['goals']
            SSAdata = datajson ['data'][11]['assists']
            SSPdata = datajson ['data'][11]['points']
            SSPPGdata = datajson ['data'][11]['pointsPerGame']
            writeHTML( "Steven Stamkos had " + str(SSGdata) + " Goals, " + str(SSAdata) + " Assists, " + str(SSPdata) + " Points and " + str(SSPPGdata)+ " Points Per Game in 2017-2018. \n")

        #                                           *-------------- GAME WINNING GOALS -----------------*

        elif StatChosen == 3:

            SSGWGdata = datajson ['data'][11]['gameWinningGoals']
            writeHTML( "Steven Stamkos had " + str(SSGWGdata) + " Game Winning Goals in 2017-2018. \n")

        #                                           *-------------- PLUS/MINUS -----------------*

        elif StatChosen == 4:

            SSPlusMdata = datajson ['data'][11]['plusMinus']
            writeHTML( "Steven Stamkos had a " + str(SSPlusMdata) + " Plus/Minus in 2017-2018. \n")        
        
        #                                           *-------------- PENALTY MINUTES -----------------*

        elif StatChosen == 5:

            SSPMdata = datajson ['data'][11]['penaltyMinutes']
            writeHTML( "Steven Stamkos had a " + str(SSPMdata) + " Penalty Minutes in 2017-2018. \n") 

        #                                           *-------------- POWER PLAY GOALS AND POINTS -----------------*

        elif StatChosen == 6:

            SSPowerPGdata = datajson ['data'][11]['ppGoals']
            SSPPPdata = datajson ['data'][11]['ppPoints']
            writeHTML( "Steven Stamkos had " + str(SSPowerPGdata) + " Power Play Goals and " + str(SSPPPdata) + " Power Play Points in 2017-2018. \n")     

        #                                           *-------------- SHORTHANDED GOALS AND POINTS -----------------*

        elif StatChosen == 7:

            SSSGdata = datajson ['data'][11]['shGoals']
            SSSPdata = datajson ['data'][11]['shPoints']
            writeHTML( "Steven Stamkos had " + str(SSSGdata) + " Shorthanded Goals and " + str(SSSPdata) + " Shorthanded Points in 2017-2018. \n")

        #                                           *-------------- FACEOFF PERCENTAGE/SHOTS/SHOOTING PERCENTGE -----------------*

        elif StatChosen == 8:

            SSFcePcgdata = datajson ['data'][11]['faceoffWinPctg']
            SSSdata = datajson ['data'][11]['shots']
            SSShtPcgdata = datajson ['data'][11]['shootingPctg']
            writeHTML( "Steven Stamkos had a " + str(SSFcePcgdata) + " Faceoff Percentage, " + str(SSSdata) + " Shots and a " + str(SSShtPcgdata) + " Shooting Percentage in 2017-2018. \n")

        #                                           *-------------- SHIFTS PER GAME AND ICE TIME -----------------*

        elif StatChosen == 9:

            SSSPGdata = datajson ['data'][11]['shiftsPerGame']
            SSTIPGdata = datajson ['data'][11]['timeOnIcePerGame']
            writeHTML( "Steven Stamkos had " + str(SSSPGdata) + " Shifts Per Game and " + str(SSTIPGdata) + " seconds on the ice per game in 2017-2018. \n")

        #                                           *-------------- PERSONAL INFO -----------------*

        elif StatChosen == 10:

            SSBDdata = datajson ['data'][11]['playerBirthDate']
            SSBCitydata = datajson ['data'][11]['playerBirthCity']
            SSBPdata = datajson ['data'][11]['playerBirthStateProvince']
            SSBCdata = datajson ['data'][11]['playerBirthCountry']
            SSNdata = datajson ['data'][11]['playerNationality']
            writeHTML( "Steven Stamkos was born on " + str(SSBDdata) + " in the city of " + str(SSBCitydata) + ", " + str(SSBPdata) + ", " + str(SSBCdata) + ". His nationality is " + str(SSNdata) + ". \n")

        #                                           *-------------- DRAFT PICK INFO -----------------*

        elif StatChosen == 11:

            SSDOPNdata = datajson ['data'][11]['playerDraftOverallPickNo']
            SSRNdata = datajson ['data'][11]['playerDraftRoundNo']
            SSDYdata = datajson ['data'][11]['playerDraftYear']
            writeHTML( "Steven Stamkos was drafted #" + str(SSDOPNdata) + " overall, in the #" + str(SSRNdata) + " round, in year " + str(SSDYdata) + ". \n") 

        #                                           *-------------- HEIGHT AND WEIGHT -----------------*

        elif StatChosen == 12:

            SSHdata = datajson ['data'][11]['playerHeight']
            SSWdata = datajson ['data'][11]['playerWeight']
            writeHTML( "Steven Stamkos is " + str(SSHdata) + " inches tall and weighs " + str(SSWdata) + " pounds. \n")

        #                                           *-------------- POSITION/SHOOTS/TEAM -----------------*

        elif StatChosen == 13:

            SSPosdata = datajson ['data'][11]['playerPositionCode']
            SSSdata = datajson ['data'][11]['playerShootsCatches']
            SSTdata = datajson ['data'][11]['playerTeamsPlayedFor']
            writeHTML( "Steven Stamkos plays " + str(SSPosdata) + "Center, Shoots " + str(SSSdata) + "ight, and played for " + str(SSTdata) + " in 2017-2018. \n")

        else:
            print("ERROR PLEASE TRY AGAIN")










                                    

                                    #*********************** MARCHAND ***********************
    elif ItemChosen == 18:

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

        StatChosen = int(input("Please make your selection. \n"))

        #                                           *--------------  GAMES PLAYED -----------------*

        if StatChosen == 1:

            BMGPdata = datajson ['data'][12]['gamesPlayed']
            writeHTML( "Brad Marchand had " + str(BMGPdata) + " Games Played in 2017-2018. \n")

        #                                           *-------------- GOALS, ASSISTS, POINTS, POINTS PER GAME -----------------*

        elif StatChosen == 2:

            BMGdata = datajson ['data'][12]['goals']
            BMAdata = datajson ['data'][12]['assists']
            BMPdata = datajson ['data'][12]['points']
            BMPPGdata = datajson ['data'][12]['pointsPerGame']
            writeHTML( "Brad Marchand had " + str(BMGdata) + " Goals, " + str(BMAdata) + " Assists, " + str(BMPdata) + " Points and " + str(BMPPGdata)+ " Points Per Game in 2017-2018. \n")

        #                                           *-------------- GAME WINNING GOALS -----------------*

        elif StatChosen == 3:

            BMGWGdata = datajson ['data'][12]['gameWinningGoals']
            writeHTML( "Brad Marchand had " + str(BMGWGdata) + " Game Winning Goals in 2017-2018. \n")

        #                                           *-------------- PLUS/MINUS -----------------*

        elif StatChosen == 4:

            BMPlusMdata = datajson ['data'][12]['plusMinus']
            writeHTML( "Brad Marchand had a " + str(BMPlusMdata) + " Plus/Minus in 2017-2018. \n")        
        
        #                                           *-------------- PENALTY MINUTES -----------------*

        elif StatChosen == 5:

            BMPMdata = datajson ['data'][12]['penaltyMinutes']
            writeHTML( "Brad Marchand had a " + str(BMPMdata) + " Penalty Minutes in 2017-2018. \n") 

        #                                           *-------------- POWER PLAY GOALS AND POINTS -----------------*

        elif StatChosen == 6:

            BMPowerPGdata = datajson ['data'][12]['ppGoals']
            BMPPPdata = datajson ['data'][12]['ppPoints']
            writeHTML( "Brad Marchand had " + str(BMPowerPGdata) + " Power Play Goals and " + str(BMPPPdata) + " Power Play Points in 2017-2018. \n")     

        #                                           *-------------- SHORTHANDED GOALS AND POINTS -----------------*

        elif StatChosen == 7:

            BMSGdata = datajson ['data'][12]['shGoals']
            BMSPdata = datajson ['data'][12]['shPoints']
            writeHTML( "Brad Marchand had " + str(BMSGdata) + " Shorthanded Goals and " + str(BMSPdata) + " Shorthanded Points in 2017-2018. \n")

        #                                           *-------------- FACEOFF PERCENTAGE/SHOTS/SHOOTING PERCENTGE -----------------*

        elif StatChosen == 8:

            BMFcePcgdata = datajson ['data'][12]['faceoffWinPctg']
            BMSdata = datajson ['data'][12]['shots']
            BMShtPcgdata = datajson ['data'][12]['shootingPctg']
            writeHTML( "Brad Marchand had a " + str(BMFcePcgdata) + " Faceoff Percentage, " + str(BMSdata) + " Shots and a " + str(BMShtPcgdata) + " Shooting Percentage in 2017-2018. \n")

        #                                           *-------------- SHIFTS PER GAME AND ICE TIME -----------------*

        elif StatChosen == 9:

            BMSPGdata = datajson ['data'][12]['shiftsPerGame']
            BMTIPGdata = datajson ['data'][12]['timeOnIcePerGame']
            writeHTML( "Brad Marchand had " + str(BMSPGdata) + " Shifts Per Game and " + str(BMTIPGdata) + " seconds on the ice per game in 2017-2018. \n")

        #                                           *-------------- PERSONAL INFO -----------------*

        elif StatChosen == 10:

            BMBDdata = datajson ['data'][12]['playerBirthDate']
            BMBCitydata = datajson ['data'][12]['playerBirthCity']
            BMBPdata = datajson ['data'][12]['playerBirthStateProvince']
            BMBCdata = datajson ['data'][12]['playerBirthCountry']
            BMNdata = datajson ['data'][12]['playerNationality']
            writeHTML( "Brad Marchand was born on " + str(BMBDdata) + " in the city of " + str(BMBCitydata) + ", " + str(BMBPdata) + ", " + str(BMBCdata) + ". His nationality is " + str(BMNdata) + ". \n")

        #                                           *-------------- DRAFT PICK INFO -----------------*

        elif StatChosen == 11:

            BMDOPNdata = datajson ['data'][12]['playerDraftOverallPickNo']
            BMRNdata = datajson ['data'][12]['playerDraftRoundNo']
            BMDYdata = datajson ['data'][12]['playerDraftYear']
            writeHTML( "Brad Marchand was drafted #" + str(BMDOPNdata) + " overall, in the #" + str(BMRNdata) + " round, in year " + str(BMDYdata) + ". \n") 

        #                                           *-------------- HEIGHT AND WEIGHT -----------------*

        elif StatChosen == 12:

            BMHdata = datajson ['data'][12]['playerHeight']
            BMWdata = datajson ['data'][12]['playerWeight']
            writeHTML( "Brad Marchand is " + str(BMHdata) + " inches tall and weighs " + str(BMWdata) + " pounds. \n")

        #                                           *-------------- POSITION/SHOOTS/TEAM -----------------*

        elif StatChosen == 13:

            BMPosdata = datajson ['data'][12]['playerPositionCode']
            BMSdata = datajson ['data'][12]['playerShootsCatches']
            BMTdata = datajson ['data'][12]['playerTeamsPlayedFor']
            writeHTML( "Brad Marchand plays " + str(BMPosdata) + "enter, Shoots " + str(BMSdata) + "eft, and played for " + str(BMTdata) + " in 2017-2018. \n")

        else:
            print("ERROR PLEASE TRY AGAIN")






                                    

                                    #*********************** BARZAL ***********************
    elif ItemChosen == 19:

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

        StatChosen = int(input("Please make your selection. \n"))

        #                                           *--------------  GAMES PLAYED -----------------*

        if StatChosen == 1:

            MBGPdata = datajson ['data'][13]['gamesPlayed']
            writeHTML( "Matthew Barzal had " + str(MBGPdata) + " Games Played in 2017-2018. \n")

        #                                           *-------------- GOALS, ASSISTS, POINTS, POINTS PER GAME -----------------*

        elif StatChosen == 2:

            MBGdata = datajson ['data'][13]['goals']
            MBAdata = datajson ['data'][13]['assists']
            MBPdata = datajson ['data'][13]['points']
            MBPPGdata = datajson ['data'][13]['pointsPerGame']
            writeHTML( "Matthew Barzal had " + str(MBGdata) + " Goals, " + str(MBAdata) + " Assists, " + str(MBPdata) + " Points and " + str(MBPPGdata)+ " Points Per Game in 2017-2018. \n")

        #                                           *-------------- GAME WINNING GOALS -----------------*

        elif StatChosen == 3:

            MBGWGdata = datajson ['data'][13]['gameWinningGoals']
            writeHTML( "Matthew Barzal had " + str(MBGWGdata) + " Game Winning Goals in 2017-2018. \n")

        #                                           *-------------- PLUS/MINUS -----------------*

        elif StatChosen == 4:

            MBPlusMdata = datajson ['data'][13]['plusMinus']
            writeHTML( "Matthew Barzal had a " + str(MBPlusMdata) + " Plus/Minus in 2017-2018. \n")        
        
        #                                           *-------------- PENALTY MINUTES -----------------*

        elif StatChosen == 5:

            MBPMdata = datajson ['data'][13]['penaltyMinutes']
            writeHTML( "Matthew Barzal had a " + str(MBPMdata) + " Penalty Minutes in 2017-2018. \n") 

        #                                           *-------------- POWER PLAY GOALS AND POINTS -----------------*

        elif StatChosen == 6:

            MBPowerPGdata = datajson ['data'][13]['ppGoals']
            MBPPPdata = datajson ['data'][13]['ppPoints']
            writeHTML( "Matthew Barzal had " + str(MBPowerPGdata) + " Power Play Goals and " + str(MBPPPdata) + " Power Play Points in 2017-2018. \n")     

        #                                           *-------------- SHORTHANDED GOALS AND POINTS -----------------*

        elif StatChosen == 7:

            MBSGdata = datajson ['data'][13]['shGoals']
            MBSPdata = datajson ['data'][13]['shPoints']
            writeHTML( "Matthew Barzal had " + str(MBSGdata) + " Shorthanded Goals and " + str(MBSPdata) + " Shorthanded Points in 2017-2018. \n")

        #                                           *-------------- FACEOFF PERCENTAGE/SHOTS/SHOOTING PERCENTGE -----------------*

        elif StatChosen == 8:

            MBFcePcgdata = datajson ['data'][13]['faceoffWinPctg']
            MBSdata = datajson ['data'][13]['shots']
            MBShtPcgdata = datajson ['data'][13]['shootingPctg']
            writeHTML( "Matthew Barzal had a " + str(MBFcePcgdata) + " Faceoff Percentage, " + str(MBSdata) + " Shots and a " + str(MBShtPcgdata) + " Shooting Percentage in 2017-2018. \n")

        #                                           *-------------- SHIFTS PER GAME AND ICE TIME -----------------*

        elif StatChosen == 9:

            MBSPGdata = datajson ['data'][13]['shiftsPerGame']
            MBTIPGdata = datajson ['data'][13]['timeOnIcePerGame']
            writeHTML( "Matthew Barzal had " + str(MBSPGdata) + " Shifts Per Game and " + str(MBTIPGdata) + " seconds on the ice per game in 2017-2018. \n")

        #                                           *-------------- PERSONAL INFO -----------------*

        elif StatChosen == 10:

            MBBDdata = datajson ['data'][13]['playerBirthDate']
            MBBCitydata = datajson ['data'][13]['playerBirthCity']
            MBBPdata = datajson ['data'][13]['playerBirthStateProvince']
            MBBCdata = datajson ['data'][13]['playerBirthCountry']
            MBNdata = datajson ['data'][13]['playerNationality']
            writeHTML( "Matthew Barzal was born on " + str(MBBDdata) + " in the city of " + str(MBBCitydata) + ", " + str(MBBPdata) + ", " + str(MBBCdata) + ". His nationality is " + str(MBNdata) + ". \n")

        #                                           *-------------- DRAFT PICK INFO -----------------*

        elif StatChosen == 11:

            MBDOPNdata = datajson ['data'][13]['playerDraftOverallPickNo']
            MBRNdata = datajson ['data'][13]['playerDraftRoundNo']
            MBDYdata = datajson ['data'][13]['playerDraftYear']
            writeHTML( "Matthew Barzal was drafted #" + str(MBDOPNdata) + " overall, in the #" + str(MBRNdata) + " round, in year " + str(MBDYdata) + ". \n") 

        #                                           *-------------- HEIGHT AND WEIGHT -----------------*

        elif StatChosen == 12:

            MBHdata = datajson ['data'][13]['playerHeight']
            MBWdata = datajson ['data'][13]['playerWeight']
            writeHTML( "Matthew Barzal is " + str(MBHdata) + " inches tall and weighs " + str(MBWdata) + " pounds. \n")

        #                                           *-------------- POSITION/SHOOTS/TEAM -----------------*

        elif StatChosen == 13:

            MBPosdata = datajson ['data'][13]['playerPositionCode']
            MBSdata = datajson ['data'][13]['playerShootsCatches']
            MBTdata = datajson ['data'][13]['playerTeamsPlayedFor']
            writeHTML( "Matthew Barzal plays " + str(MBPosdata) + "enter, Shoots " + str(MBSdata) + "ight, and played for " + str(MBTdata) + " in 2017-2018. \n")

        else:
            print("ERROR PLEASE TRY AGAIN")









                                    #*********************** VORÁCEK ***********************
    elif ItemChosen == 20:

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

        StatChosen = int(input("Please make your selection. \n"))

        #                                           *--------------  GAMES PLAYED -----------------*

        if StatChosen == 1:

            JVGPdata = datajson ['data'][14]['gamesPlayed']
            writeHTML( "Jakub Vorácek had " + str(JVGPdata) + " Games Played in 2017-2018. \n")

        #                                           *-------------- GOALS, ASSISTS, POINTS, POINTS PER GAME -----------------*

        elif StatChosen == 2:

            JVGdata = datajson ['data'][14]['goals']
            JVAdata = datajson ['data'][14]['assists']
            JVPdata = datajson ['data'][14]['points']
            JVPPGdata = datajson ['data'][14]['pointsPerGame']
            writeHTML( "Jakub Vorácek had " + str(JVGdata) + " Goals, " + str(JVAdata) + " Assists, " + str(JVPdata) + " Points and " + str(JVPPGdata)+ " Points Per Game in 2017-2018. \n")

        #                                           *-------------- GAME WINNING GOALS -----------------*

        elif StatChosen == 3:

            JVGWGdata = datajson ['data'][14]['gameWinningGoals']
            writeHTML( "Jakub Vorácek had " + str(JVGWGdata) + " Game Winning Goals in 2017-2018. \n")

        #                                           *-------------- PLUS/MINUS -----------------*

        elif StatChosen == 4:

            JVPlusMdata = datajson ['data'][14]['plusMinus']
            writeHTML( "Jakub Vorácek had a " + str(JVPlusMdata) + " Plus/Minus in 2017-2018. \n")        
        
        #                                           *-------------- PENALTY MINUTES -----------------*

        elif StatChosen == 5:

            JVPMdata = datajson ['data'][14]['penaltyMinutes']
            writeHTML( "Jakub Vorácek had a " + str(JVPMdata) + " Penalty Minutes in 2017-2018. \n") 

        #                                           *-------------- POWER PLAY GOALS AND POINTS -----------------*

        elif StatChosen == 6:

            JVPowerPGdata = datajson ['data'][14]['ppGoals']
            JVPPPdata = datajson ['data'][14]['ppPoints']
            writeHTML( "Jakub Vorácek had " + str(JVPowerPGdata) + " Power Play Goals and " + str(JVPPPdata) + " Power Play Points in 2017-2018. \n")     

        #                                           *-------------- SHORTHANDED GOALS AND POINTS -----------------*

        elif StatChosen == 7:

            JVSGdata = datajson ['data'][14]['shGoals']
            JVSPdata = datajson ['data'][14]['shPoints']
            writeHTML( "Jakub Vorácek had " + str(JVSGdata) + " Shorthanded Goals and " + str(JVSPdata) + " Shorthanded Points in 2017-2018. \n")

        #                                           *-------------- FACEOFF PERCENTAGE/SHOTS/SHOOTING PERCENTGE -----------------*

        elif StatChosen == 8:

            JVFcePcgdata = datajson ['data'][14]['faceoffWinPctg']
            JVSdata = datajson ['data'][14]['shots']
            JVShtPcgdata = datajson ['data'][14]['shootingPctg']
            writeHTML( "Jakub Vorácek had a " + str(JVFcePcgdata) + " Faceoff Percentage, " + str(JVSdata) + " Shots and a " + str(JVShtPcgdata) + " Shooting Percentage in 2017-2018. \n")

        #                                           *-------------- SHIFTS PER GAME AND ICE TIME -----------------*

        elif StatChosen == 9:

            JVSPGdata = datajson ['data'][14]['shiftsPerGame']
            JVTIPGdata = datajson ['data'][14]['timeOnIcePerGame']
            writeHTML( "Jakub Vorácek had " + str(JVSPGdata) + " Shifts Per Game and " + str(JVTIPGdata) + " seconds on the ice per game in 2017-2018. \n")

        #                                           *-------------- PERSONAL INFO -----------------*

        elif StatChosen == 10:

            JVBDdata = datajson ['data'][14]['playerBirthDate']
            JVBCitydata = datajson ['data'][14]['playerBirthCity']
            JVBPdata = datajson ['data'][14]['playerBirthStateProvince']
            JVBCdata = datajson ['data'][14]['playerBirthCountry']
            JVNdata = datajson ['data'][14]['playerNationality']
            writeHTML( "Jakub Vorácek was born on " + str(JVBDdata) + " in the city of " + str(JVBCitydata) + ", " + str(JVBPdata) + ", " + str(JVBCdata) + ". His nationality is " + str(JVNdata) + ". \n")

        #                                           *-------------- DRAFT PICK INFO -----------------*

        elif StatChosen == 11:

            JVDOPNdata = datajson ['data'][14]['playerDraftOverallPickNo']
            JVRNdata = datajson ['data'][14]['playerDraftRoundNo']
            JVDYdata = datajson ['data'][14]['playerDraftYear']
            writeHTML( "Jakub Vorácek was drafted #" + str(JVDOPNdata) + " overall, in the #" + str(JVRNdata) + " round, in year " + str(JVDYdata) + ". \n") 

        #                                           *-------------- HEIGHT AND WEIGHT -----------------*

        elif StatChosen == 12:

            JVHdata = datajson ['data'][14]['playerHeight']
            JVWdata = datajson ['data'][14]['playerWeight']
            writeHTML( "Jakub Vorácek is " + str(JVHdata) + " inches tall and weighs " + str(JVWdata) + " pounds. \n")

        #                                           *-------------- POSITION/SHOOTS/TEAM -----------------*

        elif StatChosen == 13:

            JVPosdata = datajson ['data'][14]['playerPositionCode']
            JVSdata = datajson ['data'][14]['playerShootsCatches']
            JVTdata = datajson ['data'][14]['playerTeamsPlayedFor']
            writeHTML( "Jakub Vorácek plays " + str(JVPosdata) + "ight Wing, Shoots " + str(JVSdata) + "eft, and played for " + str(JVTdata) + " in 2017-2018. \n")

        else:
            print("ERROR PLEASE TRY AGAIN")











    else:
            print("ERROR PLEASE TRY AGAIN")
main()