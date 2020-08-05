import os
import json
import requests

class Dota2Error(Exception):
    pass

class Dota2HttpError(Dota2Error):
    pass

print("Welcome to the item analysis program\n")
print("Lets see the current items!")
apikey = os.environ.get('dota2apikey')

# See http://wiki.teamfortress.com/wiki/WebAPI for a list of available 
# interfaces and resources(methods) available.

request_url = "http://api.steampowered.com/ISteamWebAPIUtil/GetSupportedAPIList/v0001/?key=" + apikey

response = requests.get(request_url)
if response.status_code >= 400:
	if response.status_code == 401:
		raise Dota2HttpError("Unauthorized request 401. Verify API key.")
	
	if response.status_code == 503:
		raise Dota2HttpError("The server is busy or you exceeded limits. Please wait 30s and try again.")

	raise Dota2HttpError("Failed to retrieve data: %s. URL: %s" % (response.status_code, url))

print(response.json())