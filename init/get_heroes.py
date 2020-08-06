import json
import sys
sys.path.append("../common/")
import dota2api
import constants

#get the hero names and ids and save to a file for use later

print("Welcome to the Hero Getter")
print("This will get the current Heroes for Dota2")

jsonResponse = dota2api.getHeroes()
result = jsonResponse.get("result")
heroes = result.get("heroes")
myheroes = {}
	
for hero in heroes:
	name = hero.get("name").replace("npc_dota_hero_", "")
	myheroes[hero.get("id")] = name

with open(constants.FILENAME_HEROES, 'w+') as outputFile:
	json.dump(myheroes, outputFile, indent=4)