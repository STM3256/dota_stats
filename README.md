# dota_stats
Using the steam API to collect and analyze stats

## Requirements
This repository requires the useage of the [Requests library](https://github.com/psf/requests)

## SETUP
1. Get a steam API key by going [here](https://steamcommunity.com/dev/apikey)
2. Put that key in your environment variables under: `dota2apikey`
3. Run whichever analysis file you want

## One-time scripts (in order)
1. Use get_all_current_interfaces.py to create an output json file (all_steam_interfaces.json) which shows the currently supported Interfaces from Valve in their API
2. Use get_all_dota_interfaces.py to create an output json file (all_dota2_interfaces.json) which shows all the currently supported *Dota2* interfaces from Valve in their API