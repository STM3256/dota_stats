# dota_stats
Using the steam API to collect and analyze stats

## Requirements
This repository requires the useage of the [Requests library](https://github.com/psf/requests)

## SETUP
1. Get a steam API key by going [here](https://steamcommunity.com/dev/apikey)
2. Put that key in your environment variables under: `dota2apikey`
3. Run whichever analysis file you want

## One-time scripts
* Use get_all_current_interfaces.py to create an output json file which shows the currently supported Interfaces from Valve in their API