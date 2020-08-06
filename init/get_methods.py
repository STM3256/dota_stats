import json
import sys
sys.path.append("../common/")
import dota2api

outputFileName = "all_steam_interfaces.json"
print("Welcome to the API Interface Caller")
print("This will get all live interfaces from Steam")

# See http://wiki.teamfortress.com/wiki/WebAPI for a list of available 
# interfaces and resources(methods) available.

jsonResponse = dota2api.getAllInterfaces()
with open(outputFileName, 'w+') as outputFile:
	json.dump(jsonResponse, outputFile, indent=4)
