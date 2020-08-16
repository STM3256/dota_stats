import sys
sys.path.append("common/")
import dota2api
import json
import constants

#get the top live games!

#pull hero dictionary into memory
with open(constants.FILENAME_HEROES, 'r+') as inputFile:
	heroes = json.load(inputFile)

outputFileName = "live_games.json" 

jsonResponse = dota2api.getTopLiveGames()

with open(outputFileName, 'w+') as outputFile:
	json.dump(jsonResponse, outputFile, indent=4)

firstgame = jsonResponse.get("game_list")[0]
match_id = firstgame.get("match_id")
spectators = firstgame.get("spectators")
players = firstgame.get("players")
print("Match "+str(match_id)+" has "+str(spectators)+" spectators!")
playerdataoutput = []
for player in players:
	#TODO change key of heroes from string to int
	player32id = player.get("account_id")
	player64id = dota2api.convert_steamid_32bit_to_64bit(player32id)
	returnedplayers = dota2api.getPlayerSummaries(player64id)
	print(returnedplayers)
	playername = returnedplayers.get("players")[0].get("personaname")
	playerdataoutput.append(playername+" is playing as "+heroes[str(player.get("hero_id"))])


with open(outputFileName, 'w+') as outputFile:
	json.dump(jsonResponse, outputFile, indent=4)