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

        print (" Enter 13 for Position, Shoots/Catches, Team. HI \n")

        StatChosen = int(input("Please make your selection. \n"))

        if StatChosen == 1:
            NMGPdata = datajson ['data'][57]['gamesPlayed']
            print ("\n Nathan MacKinnon had " + str(NMGPdata) + " Games Played in 2017-2018. \n")

        elif StatChosen == 2:
            NMGdata = datajson ['data'][57]['goals']
            NMAdata = datajson ['data'][57]['assists']
            NMPdata = datajson ['data'][57]['points']
            NMPPGdata = datajson ['data'][57]['pointsPerGame']
            print ("\n Nathan MacKinnon had " + str(NMGdata) + " Goals, " + str(NMAdata) + " Assists, " + str(NMPdata) + " Points and " + str(NMPPGdata)+ " Points Per Game in 2017-2018. \n")

        elif StatChosen == 3:
            NMGWGdata = datajson ['data'][57]['gameWinningGoals']
            print ("\n Nathan MacKinnon had " + str(NMGWGdata) + " Game Winning Goals in 2017-2018. \n")

        elif StatChosen == 4:
            NMPlusMdata = datajson ['data'][57]['plusMinus']
            print ("\n Nathan MacKinnon had a " + str(NMPlusMdata) + " Plus/Minus in 2017-2018. \n")        
        
        elif StatChosen == 5:
            NMPMdata = datajson ['data'][57]['penaltyMinutes']
            print ("\n Nathan MacKinnon had a " + str(NMPMdata) + " Penalty Minutes in 2017-2018. \n") 

        elif StatChosen == 6:
            NMPowerPGdata = datajson ['data'][57]['ppGoals']
            NMPPPdata = datajson ['data'][57]['ppPoints']
            print ("\n Nathan MacKinnon had " + str(NMPowerPGdata) + " Power Play Goals and " + str(NMPPPdata) + " Power Play Points in 2017-2018. \n")     

        elif StatChosen == 7:
            NMSGdata = datajson ['data'][57]['shGoals']
            NMSPdata = datajson ['data'][57]['shPoints']
            print ("\n Nathan MacKinnon had " + str(NMSGdata) + " Shorthanded Goals and " + str(NMSPdata) + " Shorthanded Points in 2017-2018. \n")

        elif StatChosen == 8:
            NMFcePcgdata = datajson ['data'][57]['faceoffWinPctg']
            NMSdata = datajson ['data'][57]['shots']
            NMShtPcgdata = datajson ['data'][57]['shootingPctg']
            print ("\n Nathan MacKinnon had a " + str(NMFcePcgdata) + " Faceoff Percentage, " + str(NMSdata) + " Shots and a " + str(NMShtPcgdata) + " Shooting Percentage in 2017-2018. \n")

        elif StatChosen == 9:
            NMSPGdata = datajson ['data'][57]['shiftsPerGame']
            NMTIPGdata = datajson ['data'][57]['timeOnIcePerGame']
            print ("\n Nathan MacKinnon had " + str(NMSPGdata) + " Shifts Per Game and " + str(NMTIPGdata) + " seconds on the ice per game in 2017-2018. \n")

        elif StatChosen == 10:
            NMBDdata = datajson ['data'][57]['playerBirthDate']
            NMBCitydata = datajson ['data'][57]['playerBirthCity']
            NMBPdata = datajson ['data'][57]['playerBirthStateProvince']
            NMBCdata = datajson ['data'][57]['playerBirthCountry']
            NMNdata = datajson ['data'][57]['playerNationality']
            print ("\n Nathan MacKinnon was born on " + str(NMBDdata) + " in the city of " + str(NMBCitydata) + ", " + str(NMBPdata) + ", " + str(NMBCdata) + ". His nationality is " + str(NMNdata) + ". \n")

        elif StatChosen == 11:
            NMDOPNdata = datajson ['data'][57]['playerDraftOverallPickNo']
            NMRNdata = datajson ['data'][57]['playerDraftRoundNo']
            NMDYdata = datajson ['data'][57]['playerDraftYear']
            print ("\n Nathan MacKinnon was drafted #" + str(NMDOPNdata) + " overall, in the #" + str(NMRNdata) + " round, in year " + str(NMDYdata) + ". \n") 

        elif StatChosen == 12:
            NMHdata = datajson ['data'][57]['playerHeight']
            NMWdata = datajson ['data'][57]['playerWeight']
            print ("\n Nathan MacKinnon is " + str(NMHdata) + " inches tall and weighs " + str(NMWdata) + " pounds. \n")

        elif StatChosen == 13:
            NMPosdata = datajson ['data'][57]['playerPositionCode']
            NMSdata = datajson ['data'][57]['playerShootsCatches']
            NMTdata = datajson ['data'][57]['playerTeamsPlayedFor']
            print ("\n Nathan MacKinnon plays " + str(NMPosdata) + "enter, Shoots " + str(NMSdata) + "ight, and played for " + str(NMTdata) + " in 2017-2018. \n")







