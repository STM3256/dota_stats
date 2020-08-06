import sys
sys.path.append("common/")
import dota2api
import json

#get the top live games!

outputFileName = "live_games.json"

jsonResponse = dota2api.getTopLiveGames()
with open(outputFileName, 'w+') as outputFile:
	json.dump(jsonResponse, outputFile, indent=4)