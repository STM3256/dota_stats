import os
import json
import requests

#get the top live games!

#partnerid: The documentation does not specify what this parameter should be but it seems like numbers from 1-3 return results of live games.

apikey = os.environ.get('dota2apikey')

#TODO put these in a separate class
class Dota2Error(Exception):
    pass

class Dota2HttpError(Dota2Error):
    pass

outputFileName = "all_steam_interfaces.json"
print("Welcome to the Live Games caller")
print("This will get the Top Live games")

request_url = "http://api.steampowered.com/IDOTA2Match_570/GetTopLiveGame/v1"
parameters = {'key':apikey, 'partner':1}

response = requests.get(request_url, parameters)
if response.status_code >= 400:
	if response.status_code == 401:
		raise Dota2HttpError("Unauthorized request 401. Verify API key.")
	
	if response.status_code == 503:
		raise Dota2HttpError("The server is busy or you exceeded limits. Please wait 30s and try again.")

	raise Dota2HttpError("Failed to retrieve data: %s. URL: %s" % (response.status_code, url))
	
jsonResponse = response.json()