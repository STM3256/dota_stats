import json

# This should be a one time run script
# author: Stephen Miller

#define constants
inputFileName = "all_steam_interfaces.json"
outputFileName = "all_dota2_interfaces.json"

with open(inputFileName, 'r+') as inputFile:
	data = json.load(inputFile)

print("data obj: "+str(type(data)))
apilist = data.get("apilist")
interfaces = apilist.get("interfaces")

dota2Interfaces = []
for interface in interfaces:
	if "DOTA" in interface.get("name"):
		print(interface.get("name"))
		dota2Interfaces.append(interface)

#convert to JSON
jsonOut = json.dumps(dota2Interfaces)
print(jsonOut)

#with open(outputFileName, 'w+') as outputFile:		#
	#json.dump(jsonOut, outputFile, indent=4)