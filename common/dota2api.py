import os
import requests

class Dota2Error(Exception):
    pass

def get(url, parameters):
	response = requests.get(url, parameters)
	if response.status_code >= 400:
		if response.status_code == 401:
			raise Dota2Error("Unauthorized-Verify API key.")
		if response.status_code == 503:
			raise Dota2Error("The server is busy or you exceeded limits. Please wait and try again.")
		raise Dota2Error("Failed to retrieve data: %s. URL: %s" % (response.status_code, url))
	return response.json()
	
apikey = os.environ.get('dota2apikey')

def getHeroes():
	url = "http://api.steampowered.com/IEconDOTA2_570/GetHeroes/v1"
	parameters = {'key':apikey}
	return get(url, parameters)
