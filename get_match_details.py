import os
import json
import requests

apikey = os.environ.get('dota2apikey')

outputFileName = "temp_matchDetails.json"

#TODO put these in a separate class
class Dota2Error(Exception):
    pass

class Dota2HttpError(Dota2Error):
    pass

print("Welcome to the Match Details script")

request_url = "http://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/v1"
parameters = {'key':apikey, 'match_id': '5553006917', 'include_persona_names':False}

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