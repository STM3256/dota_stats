import os
import json
import requests

#get the hero names and ids and save to a file for use later

#partnerid: The documentation does not specify what this parameter should be but it seems like numbers from 1-3 return results of live games.

apikey = os.environ.get('dota2apikey')

#TODO put these in a separate class
class Dota2Error(Exception):
    pass

class Dota2HttpError(Dota2Error):
    pass

outputFileName = "dota_heroes.json"
print("Welcome to the Hero Getter")
print("This will get the current Heroes for Dota2")

request_url = "http://api.steampowered.com/IEconDOTA2_570/GetHeroes/v1"
parameters = {'key':apikey}

response = requests.get(request_url, parameters)
if response.status_code >= 400:
	if response.status_code == 401:
		raise Dota2HttpError("Unauthorized request 401. Verify API key.")
	
	if response.status_code == 503:
		raise Dota2HttpError("The server is busy or you exceeded limits. Please wait 30s and try again.")

	raise Dota2HttpError("Failed to retrieve data: %s. URL: %s" % (response.status_code, request_url))
	
jsonResponse = response.json()
with open(outputFileName, 'w+') as outputFile:
	json.dump(jsonResponse, outputFile, indent=4)