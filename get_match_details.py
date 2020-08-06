import sys
sys.path.append("common/")
import dota2api
import json

outputFileName = "temp_matchDetails.json"
print("Welcome to the Match Details script")

match_id = '5553006917'
jsonResponse = dota2api.getMatchDetails(match_id)
with open(outputFileName, 'w+') as outputFile:
	json.dump(jsonResponse, outputFile, indent=4)