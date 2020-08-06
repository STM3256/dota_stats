# dota_stats
Using the steam API to collect and analyze stats

## Requirements
This repository requires the useage of the [Requests library](https://github.com/psf/requests).
Install using `pip install requests`

## Setup
1. Get a steam API key by going [here](https://steamcommunity.com/dev/apikey)
2. Put that key in your environment variables under: `dota2apikey`
3. Run `init.py` from the directory it sits in. This will call the other one time scripts in the init folder to get Valve's current understanding of the game for use with other scripts (heroes, items, etc) and save those to files in the root directory. Run this script again if a new hero or item gets added/deleted.

## One-time scripts
### get_methods.py 
Creates an output json file which shows the currently supported Interfaces from Valve in their API - useful for developing
### get_dota_methods.py
Creates an output json file which shows all the currently supported **Dota2** interfaces from Valve in their API - useful for developing
### get_heroes.py
Gets the current heroes and save them in a file for later reference

## Scripts
### top_live_games.py
Displays some basic info back to the terminal about the current top games