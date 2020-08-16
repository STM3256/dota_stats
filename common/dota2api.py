import os
import requests
import json

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

def convert_steamid_64bit_to_32bit(id64):
	return str(int(id64[3:]) - 61197960265728)


def convert_steamid_32bit_to_64bit(id32):
	return"765"+str(int(id32 + 61197960265728))

def getHeroes():
	url = "http://api.steampowered.com/IEconDOTA2_570/GetHeroes/v1"
	parameters = {'key':apikey}
	return get(url, parameters)

def getAllInterfaces():
	url = "http://api.steampowered.com/ISteamWebAPIUtil/GetSupportedAPIList/v0001"
	return get(url, {'key':apikey})
	
#include_persona_names doesn't seem to do anything
def getMatchDetails(match_id):
	url = "http://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/v1"
	parameters = {'key':apikey, 'match_id': match_id, 'include_persona_names':False}
	return get(url, parameters)
	
#partnerid works if value is [1-3] but no change in response
def getTopLiveGames():
	url = "http://api.steampowered.com/IDOTA2Match_570/GetTopLiveGame/v1"
	partnerid = 1
	parameters = {'key':apikey, 'partner':partnerid}
	return get(url, parameters)
	
#steam account information
def getPlayerSummaries(steamid):
	url = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002"
	#steamids are different than dota account ids
	steamids = {steamid}
	parameters = {'key':apikey, 'steamids':steamids}
	return get(url, parameters)
	
	#steam account information
def getTournamentPlayerStats(input_account_id):
	url = "http://api.steampowered.com/IDOTA2Match_570/GetTournamentPlayerStats/v1"
	account_id = {input_account_id}
	print('puppeys account => 87278757')
	parameters = {'key':apikey, 'account_id':'87278757', 'hero_id':'66', 'league_id':'65006'}
	return get(url, parameters)
	
def getLeagueListing():
	url = "http://api.steampowered.com/IDOTA2Match_205790/GetLeagueListing/v1"
	parameters = {'key':apikey}
	return get(url, parameters)	
	
#outputFileName = "puppey_chen.json"
#jsonResponse = getTournamentPlayerStats('asdf')
#with open(outputFileName, 'w+') as outputFile:
#	json.dump(jsonResponse, outputFile, indent=4)

