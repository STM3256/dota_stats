import json
import sys
sys.path.append("../common/")
import dota2api

#get the hero names and ids and save to a file for use later

outputFileName = "heroes.json"
print("Welcome to the Hero Getter")
print("This will get the current Heroes for Dota2")

jsonResponse = dota2api.getHeroes()
with open(outputFileName, 'w+') as outputFile:
	json.dump(jsonResponse, outputFile, indent=4)