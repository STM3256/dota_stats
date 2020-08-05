import json

# This should be a one time run script
# author: Stephen Miller

#define constants, TODO move these to separate file
inputFileName = "all_steam_interfaces.json"
outputFileName = "all_dota2_interfaces.json"

with open(inputFileName, 'r+') as inputFile:
	data = json.load(inputFile)

apilist = data.get("apilist")
interfaces = apilist.get("interfaces")

dota2Interfaces = []
for interface in interfaces:
	if "IDOTA" in interface.get("name"):
		print(interface.get("name"))
		dota2Interfaces.append(interface)

with open(outputFileName, 'w+') as outputFile:
	json.dump(dota2Interfaces, outputFile, indent=4)