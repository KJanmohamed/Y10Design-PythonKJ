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

        StatChosen = int(input("Please make your selection. \n"))

        if StatChosen == 1:
            BWGPdata = datajson ['data'][8]['gamesPlayed']
            print ("\n Blake Wheeler had " + str(BWGPdata) + " Games Played in 2017-2018. \n")

        elif StatChosen == 2:
            BWGdata = datajson ['data'][8]['goals']
            BWAdata = datajson ['data'][8]['assists']
            BWPdata = datajson ['data'][8]['points']
            BWPPGdata = datajson ['data'][8]['pointsPerGame']
            print ("\n Blake Wheeler had " + str(BWGdata) + " Goals, " + str(BWAdata) + " Assists, " + str(BWPdata) + " Points and " + str(BWPPGdata)+ " Points Per Game in 2017-2018. \n")

        elif StatChosen == 3:
            BWGWGdata = datajson ['data'][8]['gameWinningGoals']
            print ("\n Blake Wheeler had " + str(BWGWGdata) + " Game Winning Goals in 2017-2018. \n")

        elif StatChosen == 4:
            BWPlusMdata = datajson ['data'][8]['plusMinus']
            print ("\n Blake Wheeler had a " + str(BWPlusMdata) + " Plus/Minus in 2017-2018. \n")        
        
        elif StatChosen == 5:
            BWPMdata = datajson ['data'][8]['penaltyMinutes']
            print ("\n Blake Wheeler had a " + str(BWPMdata) + " Penalty Minutes in 2017-2018. \n") 

        elif StatChosen == 6:
            BWPowerPGdata = datajson ['data'][8]['ppGoals']
            BWPPPdata = datajson ['data'][8]['ppPoints']
            print ("\n Blake Wheeler had " + str(BWPowerPGdata) + " Power Play Goals and " + str(BWPPPdata) + " Power Play Points in 2017-2018. \n")     

        elif StatChosen == 7:
            BWSGdata = datajson ['data'][8]['shGoals']
            BWSPdata = datajson ['data'][8]['shPoints']
            print ("\n Blake Wheeler had " + str(BWSGdata) + " Shorthanded Goals and " + str(BWSPdata) + " Shorthanded Points in 2017-2018. \n")

        elif StatChosen == 8:
            BWFcePcgdata = datajson ['data'][8]['faceoffWinPctg']
            BWSdata = datajson ['data'][8]['shots']
            BWShtPcgdata = datajson ['data'][8]['shootingPctg']
            print ("\n Blake Wheeler had a " + str(BWFcePcgdata) + " Faceoff Percentage, " + str(BWSdata) + " Shots and a " + str(BWShtPcgdata) + " Shooting Percentage in 2017-2018. \n")

        elif StatChosen == 9:
            BWSPGdata = datajson ['data'][8]['shiftsPerGame']
            BWTIPGdata = datajson ['data'][8]['timeOnIcePerGame']
            print ("\n Blake Wheeler had " + str(BWSPGdata) + " Shifts Per Game and " + str(BWTIPGdata) + " seconds on the ice per game in 2017-2018. \n")

        elif StatChosen == 10:
            BWBDdata = datajson ['data'][8]['playerBirthDate']
            BWBCitydata = datajson ['data'][8]['playerBirthCity']
            BWBPdata = datajson ['data'][8]['playerBirthStateProvince']
            BWBCdata = datajson ['data'][8]['playerBirthCountry']
            BWNdata = datajson ['data'][8]['playerNationality']
            print ("\n Blake Wheeler was born on " + str(BWBDdata) + " in the city of " + str(BWBCitydata) + ", " + str(BWBPdata) + ", " + str(BWBCdata) + ". His nationality is " + str(BWNdata) + ". \n")

        elif StatChosen == 11:
            BWDOPNdata = datajson ['data'][8]['playerDraftOverallPickNo']
            BWRNdata = datajson ['data'][8]['playerDraftRoundNo']
            BWDYdata = datajson ['data'][8]['playerDraftYear']
            print ("\n Blake Wheeler was drafted #" + str(BWDOPNdata) + " overall, in the #" + str(BWRNdata) + " round, in year " + str(BWDYdata) + ". \n") 

        elif StatChosen == 12:
            BWHdata = datajson ['data'][8]['playerHeight']
            BWWdata = datajson ['data'][8]['playerWeight']
            print ("\n Blake Wheeler is " + str(BWHdata) + " inches tall and weighs " + str(BWWdata) + " pounds. \n")

        elif StatChosen == 13:
            BWPosdata = datajson ['data'][8]['playerPositionCode']
            BWSdata = datajson ['data'][8]['playerShootsCatches']
            BWTdata = datajson ['data'][8]['playerTeamsPlayedFor']
            print ("\n Blake Wheeler plays " + str(BWPosdata) + "enter, Shoots " + str(BWSdata) + "eft, and played for " + str(BWTdata) + " in 2017-2018. \n")

        else:
            print("ERROR PLEASE TRY AGAIN")