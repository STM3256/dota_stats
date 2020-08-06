# dota_stats
Using the steam API to collect and analyze stats

## Requirements
This repository requires the useage of the [Requests library](https://github.com/psf/requests).
Install using `pip install requests`

## SETUP
1. Get a steam API key by going [here](https://steamcommunity.com/dev/apikey)
2. Put that key in your environment variables under: `dota2apikey`
3. Run whichever analysis file you want

## One-time scripts (in order)
1. Run `init.py`. This will call the other one time scripts to get Valve's current understanding of the game for use with other scripts (heroes, items, etc)
* Use get_methods.py to create an output json file which shows the currently supported Interfaces from Valve in their API
* Use get_dota_methods.py to create an output json file which shows all the currently supported *Dota2* interfaces from Valve in their API
* Use get_heroes.py to get the current heroes and save them in a file