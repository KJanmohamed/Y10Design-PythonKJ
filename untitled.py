'''
myapi.py 
This is a simple program to demo using a web API with requests Python module.
Later we will add to this example to incorporate our findings into a Webpage
(HTML) format

The json library has two main functions:

json.dumps() — Takes in a Python object, and converts (dumps) it to a string.
json.loads() — Takes a JSON string, and converts (loads) it to a Python object.

'''

import requests
import json
import pprint

# Find APIs at - https://apilist.fun/

def main():

    # use API to get appropriate website info
    # this required signing up but it is free!
    myrequest = requests.get("http://www.nhl.com/stats/rest/skaters?isAggregate=false&reportType=basic&isGame=false&reportName=skatersummary&sort=[{%22property%22:%22points%22,%22direction%22:%22DESC%22},{%22property%22:%22goals%22,%22direction%22:%22DESC%22},{%22property%22:%22assists%22,%22direction%22:%22DESC%22}]&cayenneExp=gameTypeId=2%20and%20seasonId%3E=20172018%20and%20seasonId%3C=20172018")
    
    
    # The type of the return value of .json() is a dictionary, 
    # so you can access values in the object by key.

    data_json = myrequest.json()

    x = data_json['playerBirthCity']
    print (x)

    y = data_json['playerBirthCountry']
    print (y)

    # trying to grab a specific field from one of the articles....
    #z = data_json['articles'][2]

    z = data_json['playerBirthCity'][2]['playerBirthCountry']
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(z)
    #print (z)
    
 
# Here is the call to the MAIN function after we have defined when 
# the function defintions are above

main()