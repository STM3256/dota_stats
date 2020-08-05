import os
import json
import requests

print("Welcome to the item analysis program\n")
print("Lets see the current items!")
apikey = os.environ.get('dota2apikey')

# See http://wiki.teamfortress.com/wiki/WebAPI for a list of available 
# interfaces and resources(methods) available.

request_url = "http://api.steampowered.com/ISteamWebAPIUtil/GetSupportedAPIList/v0001/?key=" + apikey

allInterfaces = requests.get(request_url)
print(allInterfaces.json())