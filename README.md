# skynet_mod_bot_discord
A simple moderation bot for discord that applies filters to filter out undesirable words.

Bot Invite:
[Invite Skynet to your server!](https://discord.com/api/oauth2/authorize?client_id=748994704686710885&permissions=8&scope=bot)
This bot has a preset list of words that cannot be changed. See disclaimer at the bottom for more info.

## Overview 
This repository is meant to provide the base package of the bot, no models are included here, likewise with the bot token.
In order to get the bot working go to https://discord.com/developers/applications to get a bot token.

`intents.json` is a blank template where you can train your bot on categories, the sample one has the labeling normal, cussing and explicit for reference. 
These tags are used throughout `main.py` and modifications for the JSON structure and model must be taken into consideration.

The `.env` file has been provided as a blank template, this is where your bot token is going to be placed.

### The included Python files

`main.py` - The bot itself

`train.py` - Create the model based on `intents.json`

`training_client.py` - Allows the user to either input raw text to be split and trained, or have the bot listen in defined channels to add to `intents.json`

### Bot commands
#### !config
Makes changes to the server's configuration. So far !config is only used for setting filters.
`!config setfilter <X>`
```  
  X can be 0, 1, or 2. 
  0 - No filter
  1 - Just explicit words
  2 - Swear words and explicit words
```
---
#### !help
Shows a basic menu of usable commands.

## Requirements
This bot has been tested with python 3.6.x and requires the appropriate libraries to be installed through pip.
**Note: I used Conda to set up the specific environment and I strongly recommend doing the same if you want to clone this bot.**

### Libaries:

 `nltk`
 `pickle`
 `keras`
 `numpy`
 `dotenv`
 `discord`

# Other Info
Below is the specs of the system used to develop this bot.
This is not a list of system requirements, this is to be used as reference or for the curious.

OS: Arch Linux X86_64
Kernel: 5.12.x
CPU: AMD Ryzen 5 2600
GPU: NVIDIA GeForce RTX 2070
Memory: 15.6 GB
SWAP: 8GB


# DISCLAIMER
For the bot that you will be able to invite to your server running on my system, some of the choices of words may be biased by my opinion.
Other words may be censored by accident. This is an experimental bot, so only the message will be deleted. If there is a word that is censored for an unfair reason
please report so in issues. 



