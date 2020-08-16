import sys
sys.path.append("common/")
import dota2api
import json

outputFileName = "leagues.json"
print("printed league information here: "+outputFileName)

jsonResponse = dota2api.getLeagueListing()
with open(outputFileName, 'w+') as outputFile:
	json.dump(jsonResponse, outputFile, indent=4)