'''
myapi.py 
- simple program to demo using a web API with requests Python module
- secondary function to demo how to write out received data to an HTML file 
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

def writeHTML(data):
    myfile = open("myapi.html","w")
    myfile.write("<h1> 2017-2018 NHL SEASON STATS </h1>")
    myfile.write("<h3> THIS INCLUDES ALL THE PLAYERS IN THE NHL WITH THEIR PERSONAL STATS AND INFORMATION </h1>")
    myfile.write(data)
    myfile.close()

def main():

    # Here is the menu system
    print ("Please choose a player number")
    print ("You will be told his/her last name")

    # use API to get place info
    response = requests.get("http://www.nhl.com/stats/rest/skaters?isAggregate=false&reportType=basic&isGame=false&reportName=skatersummary&sort=[{%22property%22:%22points%22,%22direction%22:%22DESC%22},{%22property%22:%22goals%22,%22direction%22:%22DESC%22},{%22property%22:%22assists%22,%22direction%22:%22DESC%22}]&cayenneExp=gameTypeId=2%20and%20seasonId%3E=20172018%20and%20seasonId%3C=20172018")

    # if API call is correct
    if (response.status_code == 200):
        data = response.content # response comes in as byte data type
        data_as_str = data.decode()    # decode to str
        #writeHTML(data_as_str)  # call function to write string data to HTML file

        # load as a JSON to access specific data more easily
        datajson = response.json()
        MyData = datajson ['data'][0]['playerLastName']
        print (MyData)
       # BirthCountry = datajson['"playerTeamsPlayedFor"']
       # for Birthcountry in BirthCountry:
       #     print(Birthcountry)
        
    else:
        data = "Error has occured"
        writeHTML(data)

main()